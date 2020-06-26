#Breaker Selection
#本程序的运行需要Python3及以上版本
#本程序因需求只包含220KV侧、110KV侧以及10KV侧的部分断路器

import time
#220KV断路器列表
Breakers_220KV = [
	["LW1-220/2000", 220, 2000, 31.5, 80, 31.5, 4, "SF6", "户外"],
	["LW1-220/2000", 220, 2000, 40, 100, 40, 4, "SF6", "户外"],
	["LW1-220/3150", 220, 3150, 31.5, 80, 31.5, 4, "SF6", "户外"],
	["LW1-220/2500", 220, 3150, 40, 100, 40, 4, "SF6", "户外"],
	["LW2-220/2500", 220, 2500, 31.5, 80, 31.5, 4, "SF6", "户外"],
	["LW2-220/2500", 220, 2500, 40, 100, 40, 4, "SF6", "户外"],
	["LW2-220/2500", 220, 2500, 50, 125, 50, 4, "SF6", "户外"],
	["LW6-220/3150", 220, 3150, 40, 100, 40, 3, "SF6", "户外"],
	["LW6-220/3150", 220, 3150, 50, 125, 50, 3, "SF6", "户外"],
	["SFM220-220/2000", 220, 2000, 40, 80, 40, 3, "SF6", "户外"],
	["SFM220-220/2500", 220, 2500, 50, 80, 50, 3, "SF6", "户外"],
	["SFM220-220/3150", 220, 3150, 50, 100, 50, 3, "SF6", "户外"],
	["SFM220-220/4000", 220, 2000, 63, 80, 63, 3, "SF6", "户外"],
	["SFMT220-220/2000", 220, 2000, 31.5, 80, 31.5, 3, "SF6", "户外"],
	["SFMT220-220/2500", 220, 2500, 40, 100, 40, 3, "SF6", "户外"],
	["SFMT220-220/3150", 220, 3150, 50, 125, 50, 3, "SF6", "户外"],
	["SW2-220", 220, 1000, 18.4, 55, 21, 4, "少油", "户外"],
	["SW4-220", 220, 1000, 18.4, 55, 21, 5, "少油", "户外"],
	["SW6-220", 220, 1200, 21, 55, 21, 4, "少油", "户外"],
	["SW7-220", 220, 1500, 21, 55, 21, 4, "少油", "户外"]
]

#110KV断路器列表
Breakers_110KV = [
	["LW-110I/2500", 110, 2500, 31.5, 125, 50, 3, "SF6", "户外"],
	["LW6-110II/3150", 110, 3150, 40, 125, 50, 3, "SF6", "户外"],
	["SFM110-110/2000", 110, 2000, 31.5, 80, 31.5, 3, "SF6", "户外"],
	["SFM110-110/2500", 110, 2500, 40, 100, 40, 3, "SF6", "户外"],
	["SFM110-110/3150", 110, 3150, 50, 125, 50, 3, "SF6", "户外"],
	["SFM110-110/4000", 110, 4000, 50, 125, 50, 3, "SF6", "户外"],
	["SFMT110-110/2000", 110, 2000, 40, 80, 31.5, 3, "SF6", "户外"],
	["SFMT110-110/2500", 110, 2000, 50, 100, 40, 3, "SF6", "户外"],
	["SFMT110-110/3150", 110, 3150, 63, 125, 50, 3, "SF6", "户外"],
	["SW3-110", 110, 1200, 18.4, 41, 15.8, 4, "少油", "户外"],
	["SW4-110", 110, 1000, 18.4, 55, 21, 5, "少油", "户外"],
	["SW4-110G", 1000, 15.8, 55, 21, 5, "少油", "户外"],
	["SW6-110", 1200, 21, 55, 15.8, 4, "少油", "户外"],
	["SW7-110", 1200, 15.8, 55, 21, 4, "少油", "户外"]
]

#10KV断路器列表
Breakers_10KV = [
	["ZN4-10/1000", 10, 1000, 17.3, 44, 17.3, 4, "真空", "户内"],
	["ZN12-10/1250", 10, 1250, 31.5, 80, 31.5, 3, "真空", "户内"],
	["ZN12-10/1600", 10, 1600, 31.5, 80, 31.5, 3, "真空", "户内"],
	["ZN12-10/2000", 10, 2000, 40, 100, 40, 3, "真空", "户内"],
	["ZN12-10/2500", 10, 2500, 31.5, 80, 31.5, 3, "真空", "户内"],
	["ZN12-10/3150", 10, 3150, 55, 125, 50, 3, "真空", "户内"],
	["SN3-10/600", 10, 600, 11.6, 52, 20, 4, "少油", "户内"],
	["SN3-10/1000", 10, 1000, 23, 65, 23, 4, "少油", "户内"],
	["SN10-10/600", 10, 600, 28.9, 52, 20.2, 4, "少油", "户内"],
	["SN10-10/1000", 10, 1000, 28.9, 71, 29, 4, "少油", "户内"],
	["SN10-10/12500", 10, 12500, 28.9, 71, 29, 4, "少油", "户内"],
	["SN10-10/3000", 10, 3000, 28.9, 130, 13.2, 4, "少油", "户内"],
	["SN3-10/2000", 10, 2000, 29, 75, 30, 5, "少油", "户内"],
	["SN3-10/3000", 10, 3000, 29, 75, 30, 5, "少油", "户内"],
	["SN4-10G/5000", 10, 5000, 105, 300, 120, 5, "少油", "户内"],
	["SN4-10G/6000", 10, 6000, 105, 300, 120, 5, "少油", "户内"],
	["SN5-20G/6000", 10, 6000, 87, 300, 120, 5, "少油", "户内"],
	["SN5-20G/8000", 10, 8000, 87, 300, 120, 5, "少油", "户内"],
	["SN5-20G/12000", 10, 12000, 87, 300, 120, 5, "少油", "户内"],
]

#计算Qk的函数
def caculate_Qk(It, t):
	return It**2*t
	
#选择型号函数
def Select_Breaker(UN, Imax, I0s, Qk, Ish, _type, _location):
	equipments = []
		
	if UN == 220:
		if _type == 1:
			for i in range(0,16):
				if (Breakers_220KV[i][2] >= Imax and Breakers_220KV[i][3] >= I0s and \
				caculate_Qk(Breakers_220KV[i][5], Breakers_220KV[i][6]) >= Qk and \
				Breakers_220KV[i][4] >= Ish):
					equipments.append(Breakers_220KV[i])
		if _type == 2:
			for i in range(16,20):
				if (Breakers_220KV[i][2] >= Imax and Breakers_220KV[i][3] >= I0s and \
				caculate_Qk(Breakers_220KV[i][5], Breakers_220KV[i][6]) >= Qk and \
				Breakers_220KV[i][4] >= Ish):
					equipments.append(Breakers_220KV[i])
					
	if UN == 110:
		if _type == 1:
			for i in range(0,9):
				if (Breakers_110KV[i][2] >= Imax and Breakers_110KV[i][3] >= I0s and \
				caculate_Qk(Breakers_110KV[i][5], Breakers_110KV[i][6]) >= Qk and \
				Breakers_110KV[i][4] >= Ish):
					equipments.append(Breakers_110KV[i])
		if _type == 2:
			for i in range(9,14):
				if (Breakers_110KV[i][2] >= Imax and Breakers_110KV[i][3] >= I0s and \
				caculate_Qk(Breakers_110KV[i][5], Breakers_110KV[i][6]) >= Qk and \
				Breakers_110KV[i][4] >= Ish):
					equipments.append(Breakers_110KV[i])
				
	if UN == 10:
		if _type == 2:
			for i in range(6,19):
				if (Breakers_10KV[i][2] >= Imax and Breakers_10KV[i][3] >= I0s and \
				caculate_Qk(Breakers_10KV[i][5], Breakers_10KV[i][6]) >= Qk and \
				Breakers_10KV[i][4] >= Ish):
					equipments.append(Breakers_10KV[i])
		if _type == 3:
			for i in range(0,6):
				if (Breakers_10KV[i][2] >= Imax and Breakers_10KV[i][3] >= I0s and \
				caculate_Qk(Breakers_10KV[i][5], Breakers_10KV[i][6]) >= Qk and \
				Breakers_10KV[i][4] >= Ish):
					equipments.append(Breakers_10KV[i])
	
	if equipments == []:
		print("\n没有找到符合条件的断路器！\n")
		return
	
	#输出表格
	time.sleep(0.1)
	print("\n正在筛选...\n")
	time.sleep(0.3)
	title = "符合条件的断路器清单"
	name = "断路器名称"
	_UN = "UN(KV)"
	_Imax = "IN(A)"
	_INbr = "INbr(KA)"
	_ies = "ies(KA)"
	_Iq = "Iq(KA)"
	_t = "t(s)"
	_type = "断路器类型"
	_location = "使用场合"
	print("{:^125}\n".format(title))
	print("{:^20}{:12}{:11}{:13}{:^20}{:^14}{:^11}{:^6}{:^8}\n"\
	.format(name, _UN, _Imax, _INbr, _ies, _Iq, _t, _type, _location))
	for i in range(0, len(equipments)):
		print("{:^20}{:^12}{:^11}{:^16}{:^20}{:^14}{:^11}{:^10}{:^8}\n"\
		.format(equipments[i][0], equipments[i][1], equipments[i][2], \
		equipments[i][3], equipments[i][4], equipments[i][5], \
		equipments[i][6], equipments[i][7], equipments[i][8]))
	
#主函数
if __name__ == '__main__':
	while True:
		s = '请输入以下数据用于断路器的选型'
		print("{:*^25}".format(s)+'\n')
		try:
			UN = int(input("请输入额定电压 UN(KV)："))
			while UN != 220 and UN != 110 and UN != 10:
				print("⚠️本程序仅支持UN为220KV，110KV，10KV三个电压等级\n")
				input_UN_again_text = "请重新输入"
				print("{:*^25}".format(input_UN_again_text)+'\n')
				UN = int(input("请输入额定电压 UN(KV)："))
			if UN == 220 or UN == 110:
				location = 1
				print("提示💡:220KV侧以及110KV侧仅可使用户外型断路器，已自动锁定只筛选户外型\n")
				_type = int(input("请输入断路器类型(SF6断路器:1 / 少油断路器:2): "))
				while _type != 1 and _type != 2:
					print("⚠️输入有误，请重新输入！\n")
					_type = int(input("请输入断路器类型(SF6断路器:1 / 少油断路器:2): "))
			if UN == 10:
				location = 2
				print("提示💡:10KV侧仅可使用户内型断路器，已自动锁定只筛选户内型\n")
				_type = int(input("请输入断路器类型(少油断路器:2 / 真空断路器:3): "))
				while _type != 2 and _type != 3:
					print("⚠️输入有误，请重新输入！\n")
					_type = int(input("请输入断路器类型(少油断路器:2 / 真空断路器:3): "))
			Imax = float(input("请输入最大电流 Imax(A)："))
			I0s = float(input("请输入零时电流 I\'\'(KA)："))
			Qk = float(input("请输入热效应 Qk："))
			Ish = float(input("请输入冲击电流 Ish(KA)："))
			Select_Breaker(UN, Imax, I0s, Qk, Ish, _type, location)
			try:
				Input_Again = int(input("是否继续输入(是:1 / 否:0)："))
				if Input_Again == 1:
					print("\n")
					continue
				if Input_Again == 0:
					break
				else:
					print("\n⚠️输入有误，程序默认停止\n")
					break
			except ValueError:
				print("\n⚠️输入有误，程序默认停止\n")
				break
		except:
			print("⚠️输入有误，请重新输入！\n")
			continue