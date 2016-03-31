#! /usr/bin/env bash

function asr {
	echo $@ | qrencode -s 300 -o /tmp/qrcode.png && eog /tmp/qrcode.png
}