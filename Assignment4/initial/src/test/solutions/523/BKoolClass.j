.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is c Ljava/lang/String; from Label0 to Label1
.var 4 is d Z from Label0 to Label1
Label0:
	iconst_5
	istore_1
	ldc 5.1
	fstore_2
	ldc "abc"
	astore_3
	iconst_1
	istore 4
	iload_1
	invokestatic io/writeInt(I)V
	fload_2
	invokestatic io/writeFloat(F)V
	aload_3
	invokestatic io/writeStr(Ljava/lang/String;)V
	iload 4
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 2
.limit locals 5
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
