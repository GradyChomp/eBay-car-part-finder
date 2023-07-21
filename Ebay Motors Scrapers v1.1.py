import requests

def cheapestPart(apiKey, year, make, model, part):
    baseUrl = 'https://svcs.ebay.com/services/search/FindingService/v1' #don't know if this is even right
    processName = 'findItemsByKeywords'
    keywords = (f"(year, make, model, part)")
    
    headers = {
        "X-EBAY-SOA-SECURITY-APPNAME": apiKey, # don't even know
        "X-EBAY-SOA-RESPONSE-DATA-FORMAT": "json" # don't even care
        "X-EBAY-C-MARKETPLACE-ID" "EBAY-US", # what the fuck am i doing (only domestic results included)
        "X-EBAY-C-ENDUSERCTX": "affiliateCampaignId=5338432561", # please just stop (gives the greedy bastards at ebay money "for more accurate shipping")
    }

    paramaters = {
        "OPERATION-NAME":  processName,
        "keywords": keywords,
        "paginationInput.entriesPerPage": 5,
        "sortOrder": "pricePlusShippingLowest",
    }

    response = requests.get(baseUrl, headers=headers, paramaters=paramaters)
    responseJson = response.json()

    if "findItemsByKeywordsResponse" in responseJson:
        searchResult = responseJson["findItemsByKeywordsResponse"][0]
        if searchResult in searchResult:
            items = searchResult["searchResult"][0]["item"]
            if items:
                cheapestItem = items[0]
                title = cheapestItem["title"][0]
                price = cheapestItem["sellingStatus"][0]["currentPrice"][0]["__value__"]
                shipping = cheapestItem["shippingInfo"][0]["shippingServiceCost"][0]["__value__"]
                finalPrice = float(price) + float(shipping)

                print(f"The cheapest possible {part}s on eBay for a {year} {make} {model}:")
                print(f"Part: {title}")
                print(f"Price: {price}")
                print(f"Shipping: {shipping}")
                print(f"Subtotal: {finalPrice}")
                return
            
    print("Sorry, no {part} found on eBay for a {year} {make} {model}.")
    print("Try again with different criteria, or look on eBay directly.")


if __name__ == "__main__":
    apiKey = "GradyTho-Cheapest-SBX-6425bcf8a-325ba0a0"

    year = int(input("Please enter the year of your vehicle."))
    make = input("Please enter the make of your vehicle.")
    model = input("Please enter the model of your vehicle.")
    part = input("Please enter the needed part for your vechicle.")

    cheapestPart = (apiKey, year, make, model, part)