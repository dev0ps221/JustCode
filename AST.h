#pragma once
#include <queue>

enum Operator {
	InvalidOperator,
	Callgrouping,
	ArrayOperator,
	Objectaccess,
	Increment,
	Decrement,
	Negation,
	LogicalNOT,
	BitwiseNOT,
	Division,
	Multiplication,
	Modulus,
	Plus,
	Subtraction,
	Bitwiserightshift,
	Bitwiseleftshift,
	Greater,
	GEq,
	Less,
	LEQ,
	Equality,
	Inequality,
	Identity,
	NIdentity,
	BitwiseAND,
	BitwiseXOR,
	BitwiseOR,
	LogicalAND,
	LogicalOR,
	Conditionalbranch,
	Assignment,
	Multipleevaluation, //Comma
	Objectkey, //:
	ObjectStart, // {
	ObjectEnd, //}
	ArrayStart,//[
	ArrayEnd ,//]
	BracketsStart,//(
	BracketsEnd //)
};



enum  SymbolType { NullType, Newline, WhiteSpace, Symbol, Keyword, NumberLiteral, StringLiteral, VarableName,FunctionLiteral,ObjectSubReferance };



enum  StateEnum { StateNormal, StateNumber, StateVarable, StateStringLiteral, StateStringLiteralDouble, Escape, Comment, MultiLineComment };


struct ASTSymbol {
	const char* Location;
	int Lenght;
	SymbolType SymbolType;
	int SymbolValue;
};

int ProcessStream(const char* Stream, std::queue<ASTSymbol> *TokenQueue);
void DisplaySymbol(ASTSymbol symbol);
ASTSymbol ValueSymbol(int i);