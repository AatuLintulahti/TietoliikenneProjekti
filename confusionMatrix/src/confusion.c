#include <zephyr/kernel.h>
#include <math.h>
#include "confusion.h"
#include "adc.h"
#include "keskipisteet2.h"


/* 
  K-means algorithm should provide 6 center points with
  3 values x,y,z. Let's test measurement system with known
  center points. I.e. x,y,z are supposed to have only values
  1 = down and 2 = up
  
  CP matrix is thus the 6 center points got from K-means algoritm
  teaching process. This should actually come from include file like
  #include "KmeansCenterPoints.h"
  
  And measurements matrix is just fake matrix for testing purpose
  actual measurements are taken from ADC when accelerator is connected.
*/ 

int CPfake[6][3]={
	                     {1,0,0},
						 {2,0,0},
						 {0,1,0},
						 {0,2,0},
						 {0,0,1},
						 {0,0,2}
};

int measurements[6][3]={
	                     {1,0,0},
						 {2,0,0},
						 {0,1,0},
						 {0,2,0},
						 {0,0,1},
						 {0,0,2}
};

int CM[6][6]= {0};



void printConfusionMatrix(void)
{
	printk("Confusion matrix = \n");
	printk("   cp1 cp2 cp3 cp4 cp5 cp6\n");
	for(int i = 0;i<6;i++)
	{
		printk("cp%d %d   %d   %d   %d   %d   %d\n",i+1,CM[i][0],CM[i][1],CM[i][2],CM[i][3],CM[i][4],CM[i][5]);
	}
}

void makeHundredFakeClassifications(void)
{
   
   for (int j = 0; j < 6; j++)
   {
   
      for (int i = 0; i < 100; i++)
      {
         int calculatedDirection = FAKEcalculateDistanceToAllCentrePointsAndSelectWinner(measurements[j][0],measurements[j][1],measurements[j][2]);
         CM[j][calculatedDirection] = CM[j][calculatedDirection] + 1;
      }
   
   }
   
   /*******************************************
   Jos ja toivottavasti kun teet toteutuksen paloissa eli varmistat ensin,
   että etäisyyden laskenta 6 keskipisteeseen toimii ja osaat valita 6 etäisyydestä
   voittajaksi sen lyhyimmän etäisyyden, niin silloin voit käyttää tätä aliohjelmaa
   varmistaaksesi, että etäisuuden laskenta ja luokittelu toimii varmasti tunnetulla
   itse keksimälläsi sensoridatalla ja itse keksimilläsi keskipisteillä.
   *******************************************/
   printk("FAKE Classifications done\n");
}

void makeOneClassificationAndUpdateConfusionMatrix(int direction)
{
   for (int i = 0; i < 100; i++)
   {
      struct Measurement m = readADCValue();
      int calculatedDirection = calculateDistanceToAllCentrePointsAndSelectWinner(m.x,m.y,m.z);
      CM[direction][calculatedDirection] = CM[direction][calculatedDirection] + 1;
   }
   
   
   
   /**************************************
   Tee toteutus tälle ja voit tietysti muuttaa tämän aliohjelman sellaiseksi,
   että se tekee esim 100 kpl mittauksia tai sitten niin, että tätä funktiota
   kutsutaan 100 kertaa yhden mittauksen ja sen luokittelun tekemiseksi.
   **************************************/
   printk("Classifications done\n");
}

int calculateDistanceToAllCentrePointsAndSelectWinner(int x,int y,int z)
{
   float minDist = 100000;
   int closestCP;
   
   for (int i = 0; i < 6; i++)
   {
      float xDif = abs(CP[i][0] - x);
      float yDif = abs(CP[i][1] - y);
      float zDif = abs(CP[i][2] - z);

      float totalDif = xDif + yDif + zDif; 
      
      if (totalDif < minDist)
      {
         closestCP = i;
         minDist = totalDif;
      }
      
   }
   
   return closestCP;
   
   
   /***************************************
   Tämän aliohjelma ottaa yhden kiihtyvyysanturin mittauksen x,y,z,
   laskee etäisyyden kaikkiin 6 K-means keskipisteisiin ja valitsee
   sen keskipisteen, jonka etäisyys mittaustulokseen on lyhyin.
   
   
   printk("Make your own implementation for this function if you need this\n");
   ***************************************/

}

int FAKEcalculateDistanceToAllCentrePointsAndSelectWinner(int x,int y,int z)
{
   int minDist = 100000;
   int closestCP;
   
   for (int i = 0; i < 6; i++)
   {
      int xDif = abs(CPfake[i][0] - x);
      int yDif = abs(CPfake[i][1] - y);
      int zDif = abs(CPfake[i][2] - z);

      int totalDif = xDif + yDif + zDif; 
      
      if (totalDif < minDist)
      {
         closestCP = i;
         minDist = totalDif;
      }
      
   }
   
   return closestCP;
}

void resetConfusionMatrix(void)
{
	for(int i=0;i<6;i++)
	{ 
		for(int j = 0;j<6;j++)
		{
			CM[i][j]=0;
		}
	}
}

