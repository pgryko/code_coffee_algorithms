#include <gtest/gtest.h>

#include <iostream>

#include "linkedlist.hpp"

using namespace std;

TEST(Node, TestSimpleNode) {
    struct Node<std::string> node3 = {"75", nullptr};
    struct Node<std::string> node2 = {"50", &node3};
    struct Node<std::string> node1 = {"25", &node2};

    EXPECT_EQ("25", node1.data);
    EXPECT_EQ("50", node1.pNext->data);
    EXPECT_EQ("75", node1.pNext->pNext->data);

    // Test that overloaded stream operators are configured correctly
    stringstream test;
    test << node1;
    EXPECT_EQ("25", test.str());
    test >> node2;
    EXPECT_EQ("25", node2.data);

}

int main(int argc, char *argv[]) {


//    return 0;
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}