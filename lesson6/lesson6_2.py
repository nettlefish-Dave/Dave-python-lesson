#import tools
#from tools import calc_bmi,check_bmi
import edu

def main() :
    try:
        height:int = int(input('請輸入你的身高(公分 cm):'))
        weight = eval(input('請輸入你的體重(公斤 kg):'))        
        #bmicalculate = tools.calc_bmi(height,weight)
        #bmicalculate = calc_bmi(height,weight)
        bmicalculate = edu.tools.calc_bmi(height,weight)
    except ValueError:
        print('輸入發生錯誤')
    except Exception as e :
        print(e)
    else:
        print(f'你的身高:{height} 公分')
        print(f'你的體重:{weight:.2f} 公斤')
        print(f'你的 BMI值為:{bmicalculate:.2f}')
        #print(tools.check_bmi(bmicalculate))
        #print(check_bmi(bmicalculate))
        print(edu.tools.check_bmi(bmicalculate))

if __name__ == '__main__':
    main()