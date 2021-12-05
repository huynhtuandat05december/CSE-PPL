.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	bipush 7
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/writeBool(Z)V
	iconst_5
	bipush 7
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/writeBool(Z)V
	iconst_5
	bipush 7
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/writeBool(Z)V
	iconst_5
	bipush 7
	if_icmpgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/writeBool(Z)V
	iconst_5
	bipush 7
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/writeBool(Z)V
	iconst_5
	bipush 7
	if_icmpeq Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/writeBool(Z)V
Label1:
	return
.limit stack 25
.limit locals 1
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
