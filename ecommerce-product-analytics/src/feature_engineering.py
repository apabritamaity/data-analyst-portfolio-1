import pandas as pd
import numpy as np
import re

## Extract laptop specifications
def extract_specs(product_name):
    specs = {}
    
    ## Brand
    specs['brand'] = product_name.split()[0].strip()
    
    ## Processor
    cpu_match = re.search(
        r'((?:Intel|AMD)[^-^(]+)',
        product_name, 
        re.IGNORECASE
    )

    specs['processor'] = (
        cpu_match.group(1).strip() 
        if cpu_match 
        else None
    )
    
    ## RAM
    ram_match = re.search(
        r'(\d+)\s*GB(?!\s*(?:SSD|HDD|EMMC))', 
        product_name, 
        re.IGNORECASE
    )

    specs['ram_gb'] = (
        int(ram_match.group(1)) 
        if ram_match 
        else None
    )
    
    ## Storage
    storage_matches = re.findall(
        r'(\d+(?:\.\d+)?)\s*(GB|TB)\s*(SSD|HDD|EMMC)', 
        product_name, 
        re.IGNORECASE
    )

    if storage_matches:

        size, unit, storage_type = storage_matches[-1]

        size = float(size)

        if unit.upper() == "TB":
            size *= 1024

        specs["storage_gb"] = int(size)

        specs["storage_type"] = storage_type.upper()

    else:

        specs["storage_gb"] = None
        specs["storage_type"] = None


    return specs


## Discount percentage
def create_discount_percentage(df):

    df["discount_pct(%)"] = round(((df["Actual price"] - df["Discount price"]) / df["Actual price"]) * 100, 2)

    return df

## Processor tier
def assign_processor_tier(cpu):

    if pd.isna(cpu):
        return None
    
    cpu = cpu.lower()

    if 'core i3' in cpu or 'ryzen 3' in cpu or 'pentium' in cpu or 'celeron' in cpu:
        return 'Entry'
    
    elif 'core i5' in cpu or 'ryzen 5' in cpu:
        return 'Mid'
    
    elif 'core i7' in cpu or 'ryzen 7' in cpu:
        return 'High'
    
    elif 'core i9' in cpu or 'ryzen 9' in cpu or 'core ultra' in cpu:
        return 'Ultra'
    
    else:
        return 'Other'
    
    
## Processor Brand
def extract_processor_brand(cpu):

    cpu = str(cpu).lower()

    if "intel" in cpu:
        return "Intel"

    elif "amd" in cpu:
        return "AMD"

    return "Other"
    

## Processor generation
def extract_processor_generation(cpu):

    cpu = str(cpu)

    match = re.search(
        r'(\d{1,2})(?:th|st|nd|rd)\s*Gen',
        cpu,
        flags=re.IGNORECASE
    )

    if match:
        return int(match.group(1))

    return 0

## Gaming laptop
def create_is_gaming(product_name):

    keywords = ["gaming", "rog", "tuf", "predator", "legion", "omen", "nitro", "cyborg", "victus", "strix"]

    product_name = str(product_name).lower()

    return int(
        any(
            keyword in product_name
            for keyword in keywords
        )
    )

## Premium brand
def create_premium_brand(brand):

    premium_brands = ["Apple", "Dell", "HP", "Lenovo", "ASUS"]

    return int(
        str(brand).title()
        in premium_brands
    )


def create_features(df):

    df = df.copy()

    # Discount Percentage
    df = create_discount_percentage(df)

    # Extract Specifications
    specs = (
        df["Product Name"]
        .apply(extract_specs)
        .apply(pd.Series)
    )

    df = pd.concat(
        [df, specs],
        axis=1
    )

    # Processor Tier
    df["processor_tier"] = (
        df["processor"]
        .apply(assign_processor_tier)
    )

    # Additional Features
    df["processor_brand"] = (
        df["processor"]
        .apply(extract_processor_brand)
    )

    df["processor_generation"] = (
        df["processor"]
        .apply(extract_processor_generation)
    )

    df["is_gaming"] = (
        df["Product Name"]
        .apply(create_is_gaming)
    )

    df["premium_brand"] = (
        df["brand"]
        .apply(create_premium_brand)
    )

    return df
