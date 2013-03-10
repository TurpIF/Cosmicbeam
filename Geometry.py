import math

class Segment:
	def __init__(x1,y1,x2,y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

def distance(x1,y1,x2,y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def maximize_vector(x1, y1, x2, y2, max):
		size = distance(x1, y1, x2, y2)
		if  size > max:
			coeff = max/size;
			x2, y2 = (x2-x1)*coeff +x1, (y2-y1)*coeff +y1
		return x2, y2

def intersect_seg_objs(seg1, seg2):
	return intersect_seg(
		seg1.x1,seg1.y1,seg1.x2,seg1.y2,
		seg2.x1,seg2.y1,seg2.x2,seg2.y2
	)
#
#def intersect(x1,y1,x2,y2,x3,y3,x4,y4):
#	c = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
#	if c == 0:
#		raise ZeroDivisionError()
#	#return {
#	#	'x':((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*x4-y3*y4))/c,
#	#	'y':((x1*y2-y1*x2)*(y1-y4)-(y1-y2)*(x3*y4-y3*x4))/c
#	#}
#	x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/c
#	y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/c
#	if x < min(x1,x2) or x > max(x1,x2) or y < min(y1,y2) or y > max(y1,y2) return None
#	
#	return x,y

def intersect_lines(x1,y1,x2,y2,x3,y3,x4,y4):
	c = ((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
	return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/c, ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/c)

def intersect_seg(x1,y1,x2,y2,x3,y3,x4,y4):
	#if not (is_in_rect(x1,y1,x3,y3,x4,y4) or is_in_rect(x2,y2,x3,y3,x4,y4)):
	#	return None
	try:
		x,y = intersect_lines(x1,y1,x2,y2,x3,y3,x4,y4)
	except ZeroDivisionError:
		return None
	#if x < min(x1,x2) or x > max(x1,x2) or y < min(y1,y2) or y > max(y1,y2) return None
	if is_in_rect(x,y,x1,y1,x2,y2) and is_in_rect(x,y,x3,y3,x4,y4):
		return x,y
	else: return None

def is_in_rect(x,y,x1,y1,x2,y2):
	return x >= min(x1,x2) and x <= max(x1,x2) and y >= min(y1,y2) and y <= max(y1,y2)

def reflect(xMirror,yMirror,xSpeed,ySpeed):
	mirrorLen = math.sqrt(xMirror*xMirror+yMirror*yMirror)
	xU = xMirror/mirrorLen
	yU = yMirror/mirrorLen
	
	projection = xU*xSpeed+yU*ySpeed
	xProj = xU * projection
	yProj = yU * projection
	
	xOrto = xSpeed - xProj 
	yOrto = ySpeed - yProj
	
	return xProj-xOrto,yProj-yOrto

def angle(x1, y1, x2, y2, x3, y3, x4, y4):
	Xa = x2 - x1
	Ya = y2 - y1
	Xb = x4 - x3
	Yb = y4 - y3
	Na = math.sqrt(Xa*Xa+Ya*Ya)
	Nb = math.sqrt(Xb*Xb+Yb*Yb)
	C = (Xa*Xb+Ya*Yb)/(Na*Nb)
	S = (Xa*Yb-Ya*Xb)
	return (1 if S > 0 else -1) * math.acos(C)	
	
