def linearsearchproduct(productList,targetProduct):
  indices=[]
  for index,product in enumerate(productList):
    if(product==targetProduct):
      indices.append(index)
  return indices
products=["shoes","boot","loafer","shoes","sandles","shoes"]
target="shoes"
target2="apples"
result=linearsearchproduct(products,target)
print(result)