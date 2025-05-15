#import tools   #module
#from tools import calc_bmi,check_bmi   #module
#import edu  #package
#from edu import tools
#from edu.tools import calc_bmi as a
#from edu.tools import check_bmi as b
from edu.tools import calc_bmi,check_bmi

def main() :
    try:
        height:int = int(input('請輸入你的身高(公分 cm):'))
        weight = eval(input('請輸入你的體重(公斤 kg):'))        
        #bmicalculate = tools.calc_bmi(height,weight)   #module
        #bmicalculate = calc_bmi(height,weight)     #module
        #bmicalculate = edu.tools.calc_bmi(height,weight)    #package
        bmicalculate = calc_bmi(height,weight)     #package
    except ValueError:
        print('輸入發生錯誤')
    except Exception as e :
        print(e)
    else:
        print(f'你的身高:{height} 公分')
        print(f'你的體重:{weight:.2f} 公斤')
        print(f'你的 BMI值為:{bmicalculate:.2f}')
        #print(tools.check_bmi(bmicalculate))   #module
        #print(check_bmi(bmicalculate))     #module
        #print(edu.tools.check_bmi(bmicalculate))    #package
        print(check_bmi(bmicalculate))     #package

if __name__ == '__main__':
    main()