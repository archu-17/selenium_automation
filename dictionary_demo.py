demo_dict={}
demo_dict1={1:20,2:45,3:50,6:67}
demo_dict2={"qa":"testurl","uat":"uaturl"}
demo_dict3={"qa":34,3:"uaturl"}
demo_dict2['prod']='produrl'
demo_dict2[1]=56
print(demo_dict2)
demo_dict2.pop(1)
# print(type(demo_dict))
# print(demo_dict2['uat'])
print(demo_dict2)