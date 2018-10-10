#include "Rectangle.h"

//Sets the dimensions of the rectangle.
//@post The dimensions of the rectangle
//    are defined.
//@param x The position of the left of this
//    rectangle on the x-axis.
//@param y The position of the top of this
//    rectangle on the y-axis.
//@param width The width of the rect.
//@param height The height of the rect.
void Rectangle::setDimensions(const float x,
                         const float y,
                         const float width,
                         const float height)
{
    _x = x;
    _y = y;
    _width = width;
    _height = height;
}

//Gets the x value for this rect.
//@param x The position of the left of this
//    rectangle on the x-axis.
//@return The _x variable.
float Rectangle::getX()
{
    return _x;
}

//Gets the y value for this rect.
//@param y The position of the top of this
//    rectangle on the x-axis.
//@return The _y variable.
float Rectangle::getY()
{
    return _y;
}

//Gets the width value for this rect.
//@param width The width of the rect.
//@return The _width variable.
float Rectangle::getWidth()
{
    return _width;
}

//Gets the height value for this rect.
//@param height The height of the rect.
//@return The _height variable.
float Rectangle::getHeight()
{
    return _height;
}

//Gets the perimeter based on the dimensions 
//    of the rectangle. 
//@return The calculated perimeter integer.
float Rectangle::getPerimeter()
{
    return (_width)*2 + (_height)*2;	
}

//Gets the area based on the dimensions 
//    of the rectangle. 
//@return The calculated area integer.
float Rectangle::getArea()
{
    return _width * _height;
}






