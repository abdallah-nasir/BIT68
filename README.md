# BIT68
### This is Task for Bit68

  NOTE (this Project is hosted for testing on Digitalocean, http://159.223.183.4/accounts/register/ ) 
  
> ### steps for life testing
1 - create account ( http://159.223.183.4/accounts/register/)

2 - copy token from response

4 - login by username and pasword (http://159.223.183.4/accounts/login/)

3 - to create product, head to (http://159.223.183.4/product/create/) 

4 - add (name , price , category ) fields in form body and token on authorization

5- to retrieve product (http://159.223.183.4/product/get/<int:id>/) with token authorizaition

6- to filter products by user (http://159.223.183.4/product/filter/?seller=...)

7 - the default order for products is by lowest price but you can order by highest price (http://159.223.183.4/product/filter/?seller=...&order=hight)
