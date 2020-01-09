To reproduce:

```
pipenv install
pylint app
````

You should see the following output:
```
************* Module app
app.py:17:15: E1101: Instance of 'relationship' has no 'name' member (no-member)

------------------------------------------------------------------
Your code has been rated at 7.06/10 (previous run: 7.06/10, +0.00)
````
