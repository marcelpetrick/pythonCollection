/**
 * @file	TODO
 *
 * Copyright (C) 2021 marcelpetrick.it
 *
 * marcelpetrick.it owns the sole copyright of the software. Under international
 * copyright laws you (1) may not make a copy of this software except for the
 * purposes of maintaining a single archive copy, (2) may not derive works
 * herefrom, (3) may not distribute this work to others. These rights are
 * provided for information clarification, other restrictions of rights may
 * apply as well.
 *
 */
 
class test
{
private:
	 int foo{1337};
public:
	int getFoo() const {
		// stupid test by inserting all found flags, which have trailing ;
		Q_NAMESPACE;
		Q_ENUM_NS;
		Q_OBJECT;
		Q_LOGGING_CATEGORY("foo");
		Q_DECLARE_OPERATORS_FOR_FLAGS(lala);
		Q_DECLARE_FLAGS(flagga);
		Q_DECLARE_FLAGS(NothingShouldChange)
		
		Q_DECLARE_LOGGING_CATEGORY("foooo");
		Q_DECLARE_METATYPE(metaT);
		Q_PROPERTY(MEMBER bla READ bla WRITE writeBla);
	}
}
