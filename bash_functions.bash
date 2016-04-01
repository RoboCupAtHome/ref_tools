#! /usr/bin/env bash

function asr {
	echo $@ | qrencode -s 300 -o "$@.png" && eog "$@.png"
}