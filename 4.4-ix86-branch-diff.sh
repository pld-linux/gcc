#!/bin/sh

export LANG=C

svn di \
	svn://gcc.gnu.org/svn/gcc/tags/gcc_4_4_0_release \
	svn://gcc.gnu.org/svn/gcc/branches/ix86/gcc-4_4-branch \
	>gcc-ix86-branch.diff
