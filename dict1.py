#dict1.py

names = ['zhicheng','fengshichun','wuhao']

scores = ['100','0','99']

d = {'zhicheng':100,'fengshichun':0,'wuhao':99}

print d

d['xiongkai'] = 101
print d

print d['zhicheng']

d['zhicheng'] = 1000

print d['zhicheng']

print "fengshichun" in d

print "wangchengming" in d

print d.get('wuhao')
print d.get('wangjunxiang',-2)
#

d.pop('fengshichun')
print d