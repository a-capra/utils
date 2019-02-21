#!/bin/bash

{ time agana.exe /alpha/agdaq/data/run02350sub*.mid.lz4 -- --awthr 250 --diag ; } &> R2350.log&
{ time agana.exe /alpha/agdaq/data/run02350sub*.mid.lz4 -- --awthr 500 --diag ; } &> R2350.log&
{ time agana.exe /alpha/agdaq/data/run02350sub*.mid.lz4 -- --adcthr 1500 --diag ; } &> R2350.log&
{ time agana.exe /alpha/agdaq/data/run02350sub*.mid.lz4 -- --adcthr 2000 --diag ; } &> R2350.log&
{ time agana.exe /alpha/agdaq/data/run02350sub*.mid.lz4 -- --adcthr 3000 --awthr 200 --diag; } &>R2350.log&
{ time agana.exe /alpha/agdaq/data/run02350sub*.mid.lz4 -- --adcthr 4000 --diag ; } &> R2350.log&
{ time agana.exe /alpha/agdaq/data/run02350sub*.mid.lz4 -- --adcthr 4000 --awthr 200 --diag; } &>R2350.log&
{ time agana.exe /alpha/agdaq/data/run02350sub*.mid.lz4 -- --adcthr 4000 --awthr 250 --diag ; } &> R2350.log&
{ time agana.exe /alpha/agdaq/data/run02350sub*.mid.lz4 -- --adcthr 4000 --awthr 500 --diag ; } &> R2350.log&


{ time agana.exe /alpha/agdaq/data/run02361sub*.mid.lz4 -- --diag ; } &> R2361.log &
{ time agana.exe /alpha/agdaq/data/run02361sub*.mid.lz4 -- --adcthr 4000 --awthr 200 --diag; } &>R2361.log &
{ time agana.exe /alpha/agdaq/data/run02361sub*.mid.lz4 -- --adcthr 4000 --awthr 250 --diag; } &>R2361.log &
{ time agana.exe /alpha/agdaq/data/run02361sub*.mid.lz4 -- --adcthr 4000 --awthr 500 --diag; } &>R2361.log &

{ time agana.exe /alpha/agdaq/data/run02362sub*.mid.lz4 -- --adcthr 4000 --awthr 250 --diag; } &>R2362.log &

{ time agana.exe /alpha/agdaq/data/run02363sub*.mid.lz4 -- --diag; } &>R2363.log &
{ time agana.exe /alpha/agdaq/data/run02363sub*.mid.lz4 -- --adcthr 4000 --awthr 100 --diag; } &>R2363.log&
{ time agana.exe /alpha/agdaq/data/run02363sub*.mid.lz4 -- --adcthr 4000 --awthr 200 --diag; } &>R2363.log&

