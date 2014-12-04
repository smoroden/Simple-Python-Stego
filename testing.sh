#!/bin/bash
echo "Sky 107" 
time python hiddenPixel.py -p 107 -i sky.bmp -o sky107.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 107 -i sky107.bmp -f dnsspoof107sky.rb -m decode 
echo "Sky 363" 
time python hiddenPixel.py -p 363 -i sky.bmp -o sky363.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 363 -i sky363.bmp -f dnsspoof363sky.rb -m decode 
echo "test 107" 
time python hiddenPixel.py -p 107 -i test.jpg -o test107.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 107 -i test107.bmp -f dnsspoof107testjpg.rb -m decode 
echo "test 363" 
time python hiddenPixel.py -p 363 -i test.jpg -o test363.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 363 -i test363.bmp -f dnsspoof363testjpg.rb -m decode 
echo "white 107" 
time python hiddenPixel.py -p 107 -i white.jpg -o white107.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 107 -i white107.bmp -f dnsspoof107whitejpg.rb -m decode 
echo "white 363" 
time python hiddenPixel.py -p 363 -i white.jpg -o white363.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 363 -i white363.bmp -f dnsspoof363whitejpg.rb -m decode 
echo "Sky 20" 
time python hiddenPixel.py -p 20 -i sky.bmp -o sky20.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 20 -i sky20.bmp -f dnsspoof20sky.rb -m decode 
echo "Sky 500" 
time python hiddenPixel.py -p 500 -i sky.bmp -o sky500.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 500 -i sky500.bmp -f dnsspoof500sky.rb -m decode 
echo "test 20" 
time python hiddenPixel.py -p 20 -i test.jpg -o test20.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 20 -i test20.bmp -f dnsspoof20testjpg.rb -m decode 
echo "test 500" 
time python hiddenPixel.py -p 500 -i test.jpg -o test500.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 500 -i test500.bmp -f dnsspoof500testjpg.rb -m decode 
echo "white 20" 
time python hiddenPixel.py -p 20 -i white.jpg -o white20.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 20 -i white20.bmp -f dnsspoof20whitejpg.rb -m decode 
echo "white 500" 
time python hiddenPixel.py -p 500 -i white.jpg -o white500.bmp -f dnsspoof.rb -m encode 
time python hiddenPixel.py -p 500 -i white500.bmp -f dnsspoof500whitejpg.rb -m decode 