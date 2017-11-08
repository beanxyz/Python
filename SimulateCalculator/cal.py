#计算器作业，输入一个表达式，递归的根据正则表达式匹配，然后生成结果

import re

#一个全局变量保存每次变化之后的表达式
EXP=''

#乘除法
def mul_div(exp1):

    global EXP

    print("Mul/Div Caculation %s"%exp1)
    #正则表达式例如 2.3*-2.7
    ret=re.search('\d+\.?\d*[*/][+\-]?\d+\.?\d*',exp1)

    #如果没有匹配的，表明该表达式里面只剩下加减运算了
    if not ret:
        # print("final version: %s"%exp1)
        EXP=exp1
        return

    # print(ret.group())

    #直接根据乘除符号分割之后转换格式运算
    content=ret.group()
    if len(content.split('*'))>1:
        v1,v2=content.split('*')
        rt=float(v1)*float(v2)

    elif len(content.split('/'))>1:
        v1,v2=content.split('/')
        rt=float(v1)/float(v2)


    #分割之后重新组合成新的表达式，然后递归的执行，直到所有的乘除运算都结束
    before,temp,after=re.split('(\d+\.?\d*[*/][+/-]?\d+\.?\d*)',exp1,1)

    new_exp=before+str(rt)+after
    print("----Stage result: %s"%new_exp)

    #比如有的时候会出现两个负号的结果，如 --50-3 需要转换成50-3
    if new_exp.startswith('--'):
        new_exp=new_exp[2:]

        print("----Stage result converted: %s" % new_exp)
    mul_div(new_exp)


#加减法
def add_sub(exp1):

    global EXP
    print("Add/Sub Caculation %s" % exp1)

    #加减法的正则很容易，但是注意可能出现的组合比乘除法多；
    ret = re.search('[+/-]?\d+\.?\d*[+/-]+\d+\.?\d*', exp1)
    if not ret:
        # print("final version: %s" % exp1)
        EXP=exp1
        return

    # print(ret.group())

    content = ret.group()

    #如果是以-开头的组合

    if content.startswith('-'):
        #比如 -1+2 or -1+-2
        if len(content.split('+')) > 1:
            v1, v2 = content.split('+')
            rt = float(v1) +float(v2)

        #比如 -1-2 ,会被拆分成'',1,2,相当于 1+2=3，然后转换为-3
        elif len(content.split('-')) > 1:

            v1, v2,v3= re.split('-',content,2)


            rt = float(v2) + float(v3)
            rt = '-'+str(rt)



    #如果没有-的组合

    else:
        # 1+2 or 1+-2
        if len(content.split('+')) > 1:
            v1, v2 = content.split('+')
            rt = float(v1) +float(v2)

        #1--2, 可以拆成1，-2， 然后直接相减就行了;如果是4---19 ，可以拆除4，--9，然后--9取9
        elif len(content.split('-')) > 1:

            v1, v2 = re.split('-',content,1)

            if v2.startswith('--'):
                rt=float(v1)-float(v2[2])

            else:
                rt = float(v1) - float(v2)

    # print(rt)

    #加减法肯定是按顺序从左到右执行的，所以根据索引位置切片就能找到after后半截了
    after=exp1[len(content):]

    new_exp = str(rt) + after


    print("----Stage result: %s" % new_exp)
    #和乘除法一样，递归的调用直到所有的加减号都去掉

    add_sub(new_exp)


#执行程序，先乘除，后加减
def run(exp1):
    global EXP
    # print('Original expression %s' % exp1)
    mul_div(exp1)
    # print('After mul_div expression %s'%exp)
    add_sub(EXP)
    return EXP

#寻找单括号
def bracket(exp1):

    #例如 （-2.3*3.3-3.2+222）
    #如果没有单括号了，那么就表示结束了，直接返回值
    p=re.compile('\(([\+\-\*\/]*\d+\.*\d*){2,}\)')

    if not p.search(exp1):
        run(exp1)
        return EXP

    content = p.search(exp1).group()


    v1,v2,v3 = p.split(exp1, 1)

    print('before：', exp1)
    content = content[1:len(content) - 1]

    #计算括号里面的值
    ret = run(content)

    print('%s=%s' % (content, ret))
    expression = "%s%s%s" % (v1, ret, v3)
    print('after：', expression)
    print("-"*40)

    return bracket(expression)


if __name__ == "__main__":
    # inpt = "1-2.3*33-(2-33/2.3)+(2*1.2-(2*3-45.2))/20.4"
    inpt='-0.2*0.22-(3.3/23.5-22*23)+2*(1-(1.3*(2/25-2*(2.3-1)))'
    # inpt=input('Please input a expression:')
    inpp = re.sub('\s*', '', inpt)

    result = bracket(inpp)
    print("The result is: %s"%result)