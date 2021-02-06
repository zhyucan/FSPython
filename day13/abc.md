1. 简述 *args, **kwargs 的作用。（1分）

2. 看代码写结果：（5分）

   ```python
   l = [1,2,3]
   d = {"a":7,"b":8}

   def f(arg1,arg2,*args,**kwargs):
       print(arg1,arg2,args,kwargs)
       
   f(1,2,3,"groovy")
   f(arg1=1,arg2=2,c=3,zzz="h1")
   f(1,2,3,a=1,b=2,c=3)
   f(*l,**d)
   f(1,2,*l,q="winning",**d)
   ```