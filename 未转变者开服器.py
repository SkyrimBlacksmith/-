#!/usr/bin/env python
# -*- coding: utf-8 -*-

from glob import * 
from Tkinter import * 
import os

a = 0;

#函数申明部分
def start_server():
	address = tip.get();
	cmd = address + '\Unturned.exe -nographics -batchmode -nosync +secureserver/server';
	os.system(cmd);
	return a

def about():
	about_win = Toplevel();
	about_win.geometry('200x200');
	about_text = Label(about_win, text=u'本软件由晴空一鹤制作');
	about_text.pack();
	return a

def option():
	#切换地址部分
	address = tip.get();
	#切换ui部分
	options.pack();
	start.pack_forget();
	os.chdir(address + '\Servers\server\Server');
	return a

def write():
	os.remove('Commands.dat');   #移除原有的Commands.dat
	op = open('Commands.dat', 'wb');   #创建新的Commands.dat
	#作弊写入部分
	if cheat.get() == 1:
		op.write('cheats\n');
	#模式写入部分
	if mode.get() == u'PVP':
		op.write('pvp\n');
	else:
		op.write('pve\n');
	#难度写入部分
	if diffculty.get() == u'简单':
		op.write('easy\n');
	elif diffculty.get() == u'普通':
		op.write('normal\n');
	else:
		op.write('hard\n');
	#地图写入部分
	if maps.get() == u'爱德华王子岛':
		op.write('PEI\n');
	elif maps.get() == u'华盛顿':
		op.write('Washington\n');
	elif maps.get() ==u'德国':
		op.write('Germany');
	elif maps.get() == u'俄罗斯':
		op.write('Russia');
	else:
		op.write('Yukon');
	#名字写入部分
	op.write('name ');
	op.write(unicode(name.get()).encode('utf-8'));
	op.write('\n');
	#端口写入部分
	if type(port.get()) == int:
		op.write('port ');
		op.write(port.get());
		op.write('\n');
	else:
		op.write('port 25565\n');
	#最大玩家数写入部分
	if type(max_p.get()) == int:
		op.write('maxplayers ');
		op.write(max_p.get());
		op.write('\n');
	else:
		op.write('maxplayers 5\n');
	#密码写入部分
	if type(password) == int:
		op.write('password ');
		op.write(password.get());
		op.write('\n');
	#还原开始菜单部分
	options.pack_forget();
	start.pack();
	return a
	
def back():
	#还原开始菜单部分
	options.pack_forget();
	start.pack();
	return a

def tips():
	#提示ui
	tip_win = Toplevel();

#搭建gui
win = Tk();
win.title(u'未转变者一键开服器');
win.geometry('400x300');
start = Frame();
#创建提示
tip = StringVar();   
tip.set(u'在这里输入未转变者的安装地址');
#创建地址栏
enter = Entry(start, textvariable=tip).pack();
#创建开服按钮
open_server = Button(start, text=u'开启服务器', command=start_server).pack();
#添加顶部菜单
menubar = Menu(win);
menubar.add_command(label=u'关于', command=about);
menubar.add_command(label=u'服务器设置', command=option);
win.config(menu=menubar);
start.pack();

#服务器设置gui组件
options = Frame(height=200, width=200);
#服务器名称设置
name = StringVar();
name.set(u'在这里输入服务器名字');
server_name = Entry(options, textvariable=name).pack();  
#服务器端口设置
port = StringVar();
port.set(u'在这里输入服务器端口');
server_port = Entry(options, textvariable=port).pack();
#最大玩家数设置
max_p = StringVar();
max_p.set(u'在这里输入最大玩家数量');
max_player = Entry(options, textvariable=max_p).pack();   
#服务器密码设置
password = StringVar();
password.set(u'这里输入服务器密码(没有则留空)');
server_password = Entry(options, textvariable=password).pack();
#难度设置
diffculty = StringVar();
diffculty.set('请选择难度');
diffcults = OptionMenu(options, diffculty, u'简单', u'普通', u'困难').pack();
#作弊设置
cheat = IntVar();
cheat_change = Checkbutton(options, text=u'作弊', variable=cheat).pack();
#模式设置
mode = StringVar();
mode.set('请选择服务器模式');
modes = OptionMenu(options, mode, u'PVP', u'PVE').pack();
#地图设置
maps = StringVar();
maps.set('请选择服务器地图');
choose_maps = OptionMenu(options, maps, u'爱德华王子岛', u'华盛顿', u'德国', u'俄罗斯', u'育空').pack();
#更改
cannel_change = Button(options, text=u'取消更改', command=back).pack();
save_change = Button(options, text=u'保存更改', command=write).pack();

win.mainloop();