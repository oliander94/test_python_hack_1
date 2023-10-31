"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    result = [1,2,3]
    result_len = len(result)
    while_control = 0
    while while_control != result_len * 2:
        while_control+=1;
        if(while_control % 2 == 0 ):
            result.insert(while_control-1,"@")
    return result  