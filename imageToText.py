#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytesseract


# In[2]:


import pytesseract as tess


# In[4]:


tess.pytesseract.tesseract_cmd = r'C:\Users\chaud\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


# In[3]:


from PIL import Image


# In[15]:


img = Image.open('C://Users//chaud//Desktop//imgConvrt//download.png')
output = tess.image_to_string(img, lang = 'eng')

print(output)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




