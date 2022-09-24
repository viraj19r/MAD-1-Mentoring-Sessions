from jinja2 import Template
import random


def random_order_generator(n,products):   #this is the function to create dummy orders
    l=[]
    months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
    while len(l)<n:
        d={}
        d['product']=products[random.randint(0,3)]
        d['quantity']=random.randint(1,10)
        d['tracking_id']=random.randint(1000000000,9999999999)
        d['date']=f'{months[random.randint(0,11)]} {random.randint(1,28)}, 2022'
        d['total']=d['product']['price']*d['quantity']
        l.append(d)
    return l


def main():
    
    seller_1={'email':'seller_1@example.com','profile_img':'img1.jpg','shop_name':'Seller 1 Enterprises',
    'shop_owner':'Mr. Xyz','logo':'logo1.png','shop_address':'Seller 1 Enterprises, Opp. something something something something',
    'pan_no':'ANJ8120AAA', 'about':'we are seller based Xyz place and our main product is Xyz'}
    
    seller_2={'email':'seller_2@example.com','profile_img':'img2.jpg','shop_name':'Seller 2 Enterprises',
    'shop_owner':'Ms. Abc','logo':'logo2.png','shop_address':'Seller 2 Enterprises, Opp. something something something',
    'pan_no':'CPD8120BADCS','about':'we are seller based Abc place and our main product is Abc'}
    
    products=[
        {'name':'Lamp','model':'AX-21','price':2199,'stock':50,'sold':7,'discount':15,'img':'img1.webp','id':'123-0000-12'},
        {'name':'Stool','model':'BX-52','price':1249,'stock':25,'sold':10,'discount':7,'img':'img2.png','id':'145-0045-78'},
        {'name':'Chair','model':'KX-96','price':2599,'stock':35,'sold':6,'discount':5,'img':'img3.png','id':'196-0542-14'},
        {'name':'Table','model':'ZX-86','price':5999,'stock':55,'sold':12,'discount':9,'img':'img4.png','id':'842-1450-96'}
        ]
    
    orders=random_order_generator(50,products) #change 50 with any number to increace and decrease number of orders being generated

    seller=seller_1   #there is 2 seller_1 and seller_2 you can change if you want

    html_template_file=open('index_html_template.html.jinja2','r')  #index page template
    html_template=html_template_file.read()
    t=Template(html_template)
    output=t.render(seller=seller)
    g=open('index.html','w')
    g.write(output)
    html_template_file.close()
    g.close()

    html_template_file=open('products_html_template.html.jinja2','r') #product page template
    html_template=html_template_file.read()
    t=Template(html_template)
    output=t.render(products=products,seller=seller)
    g=open('products.html','w')
    g.write(output)
    html_template_file.close()
    g.close()

    html_template_file=open('orders_html_template.html.jinja2','r') #order page template
    html_template=html_template_file.read()
    t=Template(html_template)
    output=t.render(seller=seller,orders=orders)
    g=open('orders.html','w')
    g.write(output)
    html_template_file.close()
    g.close()



if __name__=='__main__':
    main()