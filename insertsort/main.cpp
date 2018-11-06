#include <iostream>
#include <gtest/gtest.h>
//https://www.eriksmistad.no/getting-started-with-google-test-on-ubuntu

struct BankAccount
{
    int balance = 0;

    BankAccount()
    {

    }

    explicit BankAccount(const int balance)
    : balance{balance}
    {


    }
};

TEST(AccountTest, BankAccountStartsEmpty)
{
    BankAccount account;
    EXPECT_EQ(0,account.balance);
}

int main(int argc, char* argv[]) {
//std::cout << "Hello, World!" << std::endl;
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}