from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# Driver params
DRIVER_PATH = "C:\\EdgeWebDriver\\msedgedriver.exe"
# Setup driver, use web driver for correct build version of edge installed.
# https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
driver = webdriver.Edge(executable_path=DRIVER_PATH)

# list of pages to check
gcStorePages = [
    "https://www.bestbuy.com/site/msi-geforce-rtx-3080-ventus-3x-10g-oc-bv-gddr6x-pci-express-4-0-graphic-card-black-silver/6430175.p?skuId=6430175",
    "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-gaming-x-trio-10g/p/N82E16814137597?Description=MSI%20GeForce%20RTX%203080%20DirectX%2012%20RTX%203080&cm_re=MSI_GeForce%20RTX%203080%20DirectX%2012%20RTX%203080-_-14-137-597-_-Product",
    "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g-oc/p/N82E16814137598?Description=MSI%20GeForce%20RTX%203080%20DirectX%2012%20RTX%203080&cm_re=MSI_GeForce%20RTX%203080%20DirectX%2012%20RTX%203080-_-14-137-598-_-Product",
    "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g/p/N82E16814137600?Description=MSI%20GeForce%20RTX%203080%20DirectX%2012%20RTX%203080&cm_re=MSI_GeForce%20RTX%203080%20DirectX%2012%20RTX%203080-_-14-137-600-_-Product",
    # "https://www.bhphotovideo.com/c/product/1593997-REG/msi_g3080v3x10c_geforce_rtx_3080_ventus.html",
    # "https://www.bhphotovideo.com/c/product/1593996-REG/msi_g3080gxt10_geforce_rtx_3080_gaming.html",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card/6436196.p?skuId=6436196",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card/6436196.p?skuId=6436196",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card/6436194.p?skuId=6436194",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card/6432399.p?skuId=6432399",
    "https://www.bestbuy.com/site/evga-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card/6432400.p?skuId=6432400",
    "https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?skuId=6432445",
    "https://www.newegg.com/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457?Description=3080&cm_re=3080-_-14-126-457-_-Product",
    "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3883-kr/p/N82E16814487521?Description=3080&cm_re=3080-_-14-487-521-_-Product",
    # "https://www.evga.com/products/product.aspx?pn=10G-P5-3895-KR",
    # "https://www.evga.com/products/product.aspx?pn=10G-P5-3897-KR",
    # "https://www.evga.com/products/product.aspx?pn=10G-P5-3883-KR",
    # "https://www.evga.com/products/product.aspx?pn=10G-P5-3885-KR",
    "https://www.newegg.com/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457",
    "https://store.asus.com/us/item/202009AM290000002/ASUS-ROG-STRIX-NVIDIA-GeForce-RTX-3080-OC-Edition-Gaming-Graphics-Card-%28PCIe-4.0%2C-10GB-GDDR6X%2C-HDMI-2.1%2C-DisplayPort-1.4a%2C-Axial-tech-Fan-Design%2C-2.9-slot%2C-Super-Alloy-Power-II%2C-GPU-Tweak-II%29"
]

# Potential button id's
aTCButtonClassNames = [
    'add-to-cart-button',
    'call-to-action-main-product',
    'toCartBtn',
    'add-to-cart',
    'AddToChat',
    'btn-addcart'   
]
# Button Markup used
buttonType = {
    "bhphotovideo":"button",
    "bestbuy":"button",
    "newegg":"div",
    "adorama":"button",
    "evga": "span",
    "store.asus":"button"
}
# Supported Sites
websiteNames = [
    "bhphotovideo",
    "bestbuy",
    "newegg",
    "adorama",
    "evga",
    "store.asus"
]
# check if current url is in list of supported sites, if it is return the name of the site.
def getWebsiteName():
    for name in websiteNames:
        if name in driver.current_url:
            return name
# locate add to cart button and return the element if found
def findAddToCartButton():
    elementType = buttonType[getWebsiteName()]
    try:
        for buttonClassName in aTCButtonClassNames:
            try:
                Button = driver.find_element_by_xpath(f"//{elementType}[contains(@class,'{buttonClassName}')]")
                fullButtonClassName = Button.get_attribute("class")
            except NoSuchElementException:
                print(f'couldn\'t find button with class name \"{buttonClassName}\"')
            else:
                print(f'found button with class name \"{fullButtonClassName}\"')
                break
        try:
            Button
        except Exception:
            raise Exception()

    except Exception:
        print("Couldn't Find Add to Cart Button")
    else:
        print("Found Add To Cart Button")
        return Button
# does the button label contain add to cart?
def addToCartAvailable(button):
    try:
        if 'add to cart' in button.text.lower():
            return True
        else:
            return False
    except Exception:
        return False
# main program loop
def main():
    # Check pages for add to cart button
    inStock = False

    while ( not inStock):
        for page in gcStorePages:
            driver.get(page)
            print(f'checking {driver.current_url}')
            aTCButton = findAddToCartButton()
            if addToCartAvailable(aTCButton):
                print("Add to Cart Button Present!")
                inStock = True
                driver.execute_script("window.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ');")
                break
            else:
                print("Add to Cart Button Not Present Or Disabled")
    input()                
    driver.quit()

if __name__ == "__main__":
    main()
