.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is d Z from Label0 to Label1
Label0:
	fconst_1
	invokestatic io/writeFloat(F)V
	ldc "abc"
	invokestatic io/writeStr(Ljava/lang/String;)V
	iconst_0
	invokestatic io/writeBool(Z)V
	iconst_1
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 5
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
