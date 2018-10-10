
#ifndef _RECTANGLE
#define _RECTANGLE

#include "Shape.h"

class Rectangle: public Shape
{
private:
	float _x, _y, _width, _height;
public:
	void setDimensions(const float x,
                         const float y,
                         const float width,
                         const float height);
	float getX();
	float getY();
	float getWidth();
	float getHeight();
	virtual float getPerimeter();
	virtual float getArea();
};

#endif
