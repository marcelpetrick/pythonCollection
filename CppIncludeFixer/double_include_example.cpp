#include "BaseClass.h"

#include "../aa.h"
#include "../bb.h"
#include "../cc_double.h" // double

#include "dd.h"
#include "ee.h" // double
#include "ff.h"
#include "cc_double.h" // double

#include "gg.h"
#include "dd.h" // double

// Qt
#include <QFont>
#include <QTextDocument>
#include <QtWidgets/QGraphicsSceneMouseEvent>
#include <QtWidgets/QGraphicsTextItem>

BaseClass::BaseClass(QObject *in_parent)
    : QGraphicsScene(in_parent)
{
	// blubb
}

BaseClass::~BaseClass()
{
	// blubb
}
