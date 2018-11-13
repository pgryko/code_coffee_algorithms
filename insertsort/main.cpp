#include <iostream>
#include <array>
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

// Input 5,4,2,1,6,3,1
// Expected output 1,1,2,3,4,5,6

TEST(AccountTest, BankAccountStartsEmpty)
{
    BankAccount account;
    std::array<int,7> a1 {5,4,2,1,6,3,1};
    std::array<int,7> a2 {5,4,2,1,6,3,1};
    EXPECT_EQ(a1,a2);
}

template < typename T, size_t N > void insertsort(std::array<T, N> * Array)
{

    std::cout << "Insertsort!, array size is " << Array->size() << std::endl;

    std::cout << "Array contains " << std::endl;


    for (const auto& s : *Array)
    {
        std::cout << " " << s << ", ";
    }
    std::cout <<  std::endl;

}

int main(int argc, char* argv[]) {
std::cout << "Hello, World!" << std::endl;
    std::array<int,7> a1 {5,4,2,1,6,3,1};
    insertsort(&a1);
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}