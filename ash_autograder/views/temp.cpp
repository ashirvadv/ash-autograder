#include <iostream>

using namespace std;

int main()
{
	int secret_number = 4;
	int guess;

	cout << "What is your guess?" << endl;
	cin >> guess;

	while (guess != secret_number)
	{
		cout << "What is your guess?" << endl;
		cin >> guess;
	}

	for (int guess; guess != secret_number; )
	{
		cout << "What is your guess?" << endl;
		cin >> guess;
	}
}