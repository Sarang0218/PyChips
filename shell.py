import basic
from time import sleep
import tqdm

while True:
    text = input('chips > ')
    if text.strip() == "": continue
    if text == "setup":
      for i in tqdm.tqdm(range(0, 100), desc ="Setting Up..."):
        sleep(0.1)  
      continue
    result, error = basic.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else:
            print(repr(result))
        
