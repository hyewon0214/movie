    result.append([Title, rating, aud])
    time.sleep(3)
    search_box = driver.find_element_by_name('query')
    search_box.clear()
time.sleep(3)
print(result)
driver.close()

