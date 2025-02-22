# Locators
# ========
# ID, Name, Class Name, CSS Selector, XPath, Tag Name, Link Text, Partial Link Text
#
# ID
# ===
# <span title="RED" id="bunny" data-ng-repeat="color in colors" class="bunny productColor ng-scope RED" data-ng-hide="color.code == 'ABCDEF'" data-ng-style="color.code == 'FFFFFF' ?
#                                           {'backgroundColor': '#' + color.code, 'border': 'solid 1px #9d9d9d' } :
#                                           {'backgroundColor': '#' + color.code, 'border': 'solid 1px transparent'}" data-ng-class="{ colorSelected : colorSelected.name == color.name , RED : colorSelected.name}" data-ng-click="setColor(color, $event)" style="background-color: rgb(221, 58, 91); border: 1px solid transparent;">
#                             </span>

# driver.find_element(By.ID, "bunny")

# CSS Selector
# ============
# driver.find_element(By.CSS_SELECTOR, "span[title='Red']")
# driver.find_element(By.CSS_SELECTOR, "[title='Red']")

# Name
#======
# <input name="quantity" type="text" ng-model="numAttr" numbers-only="" class="ng-pristine ng-untouched ng-valid">
#
# driver.find_element(By.NAME, "quantity")
#
# Class Name
# ==========
# <input ng-model="first" type="text" class="input-small ng-valid ng-dirty ng-touched">
#
# driver.find_element(By.CSS_SELECTOR,"[class='input-small ng-valid ng-dirty ng-touched']")
# driver.find_element(By.CLASS_NAME,"ng-valid")
#
# <h2 class="ng-binding">10</h2>
# driver.find_element(By.CLASS_NAME, "ng-binding")
# driver.find_element(By.CSS_SELECTOR,".ng-binding")
# driver.find_element(By.CSS_SELECTOR,"h2.ng-binding")
#
# Link Text
# =========
# <a href="reservation.php" style="margin-left: 5px;color: #0000ee;text-decoration: underline;">Flights</a>
#
# driver.find_element(By.LINK_TEXT,"Flights")
#
# XPath
# =====
#
# <span title="RED" id="bunny" data-ng-repeat="color in colors" class="bunny productColor ng-scope RED" data-ng-hide="color.code == 'ABCDEF'" data-ng-style="color.code == 'FFFFFF' ?
#                                           {'backgroundColor': '#' + color.code, 'border': 'solid 1px #9d9d9d' } :
#                                           {'backgroundColor': '#' + color.code, 'border': 'solid 1px transparent'}" data-ng-class="{ colorSelected : colorSelected.name == color.name , RED : colorSelected.name}" data-ng-click="setColor(color, $event)" style="background-color: rgb(221, 58, 91); border: 1px solid transparent;">
#                             </span>
# driver.find_element(By.CSS_SELECTOR, "span[title='RED']")
# driver.find_element(By.XPATH, "//span[@title='RED']")

# //*[text()='ADD TO CART']



