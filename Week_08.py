#include <iostream>
using namespace std;

const int costPerHour = 20;
const int costHalfHour = 12;
int money = 0;
int size = 14;

string availableBoats[10][14] = {
    {"10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"},
    {"10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"},
    {"10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"},
    {"10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"},
    {"10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"},
    {"10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"},
    {"10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"},
    {"10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"},
    {"10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"},
    {"10:00","10:30","11:00","11:30","12:00","12:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30"}
};

// Function to book a boat based on the chosen duration and time
void bookBoat(int duration, string time) {
    for (int k = 0; k < 10; k++) {
        int count = -1;
        // Find the index of the selected time in the availableBoats array
        for (int i = 0; i < size; i++) {
            if (availableBoats[k][i] == time) {
                count = i;
                break;
            }
        }
        // Booking Boat for one Hour
        if (duration == 1) {
            // Shift the elements to the left to "delete" the booked time slot
            for (int j = count; j < size - 2; j++) {
                availableBoats[k][j] = availableBoats[k][j + 2];
            }
            money += costPerHour;
            cout << "Your Boat is booked for " << time << " to " << availableBoats[k][count] << ".\n" << endl;
            break;  // Stop the loop after booking
}

        // Booking Boat for Half an hour
        if (duration == 2) {
            // Shift the elements to the left to "delete" the booked time slot
            for (int j = count; j < size - 1; j++) {
                availableBoats[k][j] = availableBoats[k][j + 1];
            }
            money += costHalfHour;
            cout << "Your Boat is booked for " << time << " to " << availableBoats[k][count + 1] << ".\n" << endl;
            break;  // Stop the loop after booking
        }
    }
}

int main() {
    int duration, choice;
    string time, password;
    cout << "Welcome" << endl;
    do {
        cout << "Press 1 to Book Boat.\nPress 2 for Admin" << endl;
        cin >> choice;
        if (choice == 1) {
            cout << "Press 1 to Book Boat for 1 Hour." << endl;
            cout << "Press 2 to Book Boat for Half an Hour." << endl;
            cin >> duration;
            cout << "Choose Time" << endl;
            // Display available boat times
            for (int i = 0; i < size; i++) {
                cout << availableBoats[9][i] << " ";
            }
            cout << endl;
            cin >> time;
            if (duration == 1) {
                if (time != availableBoats[0][12]) {
                    bookBoat(duration, time);
                } else {
                    cout << "You can't book a boat before 10:00 or after 4:30 for 1 hour." << endl;
                }
            }
            if (duration == 2) {
                if (time == availableBoats[0][12]) {
                    bookBoat(duration, time);
                } else {
                    cout << "You can't book a boat before 10:00 or after 4:30 for." << endl;
                }
                bookBoat(duration, time);
            }
        }
        if (choice == 2) {
            cout << "Enter Password" << endl;
            cin >> password;
            if (password == "Admin@123") {
                cout << "Total money collected so far is " << money << endl;
                cout << "Available Boats are ";
                // Display available boat times for admin
                for (int i = 0; i < size; i++) {
                    cout << availableBoats[0][i] << "  ";
                }
                cout << endl;
            } else {
                cout << "Incorrect Password" << endl << endl;
            }
        }
    } while (true);
return 0;
}