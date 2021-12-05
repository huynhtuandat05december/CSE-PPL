.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	ldc 2.5
	fstore_1
	fconst_1
	fload_1
	fsub
	fload_1
	fsub
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
