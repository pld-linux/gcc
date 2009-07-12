#!/bin/sh

export LANG=C

svn di \
	svn://gcc.gnu.org/svn/gcc/tags/gcc_4_4_0_release \
	svn://gcc.gnu.org/svn/gcc/branches/gcc-4_4-branch \
	>gcc-branch.diff
