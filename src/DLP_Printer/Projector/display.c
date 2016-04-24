#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "VG/openvg.h"
#include "VG/vgu.h"
#include "fontinfo.h"
#include "shapes.h"

//#define DEBUG

static int width, height;


static PyObject *display_init(PyObject *self, PyObject *args){ //do this properly
//	int width, height;
	init(&width, &height);
	Start(width,height);
	#ifdef DEBUG
		printf("%dx%d\r\n",width,height);
	#endif
  Py_RETURN_NONE;
}

static PyObject *display_expose(PyObject *self, PyObject *args){
	Start(width,height); //start composing the image
	Background(0,0,0); //background is black
	PyObject *layer;
	if(!PyArg_ParseTuple(args,"O",&layer)){
		return NULL;
	}
	long count; //this is the amount of contours.
	count = PyTuple_Size(layer);
	#ifdef DEBUG
		printf("Layer has %lu contours\r\n",count);
	#endif

//	if( PyInt_Check( PyTuple_GetItem(layer,0) ) ){
//		 count = 1;
//		 #ifdef DEBUG
//			 printf("Single contour. Count is now %lu",count);
//		 #endif
//	}

	//now you have a tuple of contours.
	//Let's draw them all
	int i;//iterating variable
	for (i=0;i<count;i++){
		PyObject *contour;
//Get the proper contour
//		if(count==1){
//			contour=layer;
//		}else{
		contour = PyTuple_GetItem(layer,i);
//		}
		long color; //holds the color of the contour
		long csize; //holds the number of points
		PyObject *Xlist; //holds the x coordinates of the points
		PyObject *Ylist; //holds the y coordinates of the points
		#ifdef DEBUG
			PyRun_SimpleString("print('contour loaded')");
		#endif

		Xlist=PyTuple_GetItem(contour,1);
		Ylist=PyTuple_GetItem(contour,2);

		#ifdef DEBUG
			PyRun_SimpleString("print('contour lists loaded')");
		#endif

		//Extract size, color and coordinates of the contour.
		csize = PyList_Size(Xlist);

		#ifdef DEBUG
			printf("csize is %ld\r\n",csize);
		#endif

		color = PyInt_AsLong(PyTuple_GetItem(contour,0));//get the color

		#ifdef DEBUG
			if(color==1){
				PyRun_SimpleString("print('color is white')");
			}else{
				if(color == 0){
					PyRun_SimpleString("print('color is black')");
				}
			}
		#endif

		//Turn the tuples into c arrays
		float xpoints[csize];
		float ypoints[csize];

		long j;//iterating variable
		for(j = 0;j<csize;j++){
			PyObject *xpoint;
			PyObject *ypoint;
			xpoint = PyList_GetItem(Xlist,j);
			if(xpoint == NULL){
				PyErr_SetString(PyExc_TypeError,"xpoint is NULL");
				return NULL;
			}
			//Py_DECREF(xpoint);
			ypoint = PyList_GetItem(Ylist,j);
			if(ypoint == NULL){
				PyErr_SetString(PyExc_TypeError,"ypoint is NULL");
				return NULL;
			}
			//Py_DECREF(ypoint);
			if (!PyFloat_Check(xpoint) || !PyFloat_Check(ypoint)) {
				PyErr_SetString(PyExc_TypeError, "expected sequence of integers");
				if(xpoint == NULL || ypoint == NULL){
					PyErr_SetString(PyExc_TypeError, "something is null");
				}
				return NULL;
			}
			//put the point into the array.
			xpoints[j] = (float) PyFloat_AsDouble(xpoint);
			ypoints[j] = (float) PyFloat_AsDouble(ypoint);
			#ifdef DEBUG
				printf("Point Loaded\r\n");
			#endif
		}

		//construct the image

		VGfloat vgcolor[4];

		if(color == 1){
			RGBA(255,255,255,1,vgcolor);
		}
		else{
			RGBA(0,0,0,1,vgcolor);
		}

		setfill(vgcolor);

		#ifdef DEBUG
			int a;
			for(a=0;a<csize;a++){
				printf("%d of %d: %f\r\n",a,sizeof(xpoints),xpoints[a]);
			}
		#endif
		/*
		//turn them into floats, because that's what polygon needs
		float x[csize];
		float y[csize];


		//this could be done in a more elegant way...
		long b;
		for(b=0;b<csize;b++){
			x[b]=(float)xpoints[b];
			y[b]=(float)ypoints[b];
		}
		*/
		#ifdef DEBUG
			int e;
			for(e=0;e<4;e++){
				printf("%f\r\n",x[e]);
			}
		#endif

		VGfloat points[csize * 2];
		VGPath path = newpath();
		interleave(xpoints,ypoints,csize,points);
		VGubyte segments[csize]; //{VG_MOVE_TO_ABS , VG_LINE_TO} and so on.
		long iter;
		segments[0]= VG_MOVE_TO_ABS;
		for(iter=1;iter<csize;iter++){
			segments[iter] = VG_LINE_TO;
		}
		vgAppendPathData(path,csize,segments,points);
		vgDrawPath(path,VG_FILL_PATH);
		vgDestroyPath(path);

		//Polygon(xpoints,ypoints,csize);

		#ifdef DEBUG
			printf("first x coordinate is %f\r\n",x[0]);
		#endif
	}
//All contours loaded

	End(); //End composing the image and show.
	Py_RETURN_NONE;
}

static PyObject *display_blank(PyObject *self, PyObject *args){
	Start(width,height);
	Background(0,0,0);
	End();
	Py_RETURN_NONE;
}

static PyObject *display_finish(PyObject *self, PyObject *args){
	finish();
	Py_RETURN_NONE;
};

static PyMethodDef display_methods[] = {
	{"init", (PyCFunction)display_init, METH_NOARGS, NULL},
	{"expose", (PyCFunction)display_expose ,METH_VARARGS, NULL},
	{"finish", (PyCFunction)display_finish, METH_NOARGS, NULL},
	{"blank", (PyCFunction)display_blank, METH_NOARGS, NULL},
};

DL_EXPORT(void) initdisplay(void)
{
	Py_InitModule("display",display_methods);
}
