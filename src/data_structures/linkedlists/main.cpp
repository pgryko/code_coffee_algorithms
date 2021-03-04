#include <gtest/gtest.h>

#include <iostream>

#include "linkedlist.hpp"

using namespace std;


TEST(Node, TestSimpleNode) {
    struct Node<std::string> node = {"AA", nullptr};
    EXPECT_EQ("AA", node.data);
    EXPECT_EQ(nullptr, node.pNext);

    // Test that overloaded stream operators are configured correctly
    stringstream test;
    test << node;
    EXPECT_EQ("AA", test.str());

    struct Node<std::string> node2 = {"BB", nullptr};
    EXPECT_EQ("BB", node2.data);
    test >> node;
    EXPECT_EQ("AA", node.data);

}

TEST(Node, TestChainNodes) {
    auto node3 = std::make_shared<Node<std::string>>("75", nullptr);
    auto node2 = std::make_shared<Node<std::string>>("50", node3);
    auto node1 = std::make_shared<Node<std::string>>("25", node2);

    EXPECT_EQ("25", node1->data);
    EXPECT_EQ("50", node1->pNext->data);
    EXPECT_EQ("75", node1->pNext->pNext->data);
}


TEST(LinkedList, TestConstructor) {

    auto my_linked_list = LinkedList<std::string>();

    EXPECT_EQ(nullptr, my_linked_list.GetHeadNode());
    EXPECT_EQ(0, my_linked_list.Size());

}

TEST(LinkedList, TestPush) {

    auto my_linked_list = LinkedList<std::string>();
    EXPECT_EQ(nullptr, my_linked_list.GetHeadNode());

    auto elements = std::array{"1","2","3","4"};

    for (const auto& elem : elements){
        my_linked_list.Push(elem);
    }
    EXPECT_EQ(4, my_linked_list.Size());

    std::reverse(elements.begin(),elements.end());
    auto pCrawler = my_linked_list.GetHeadNode();
    for (const auto& elem : elements){
        EXPECT_EQ(elem, pCrawler->data);
        pCrawler = pCrawler->pNext;
    }
}

int main(int argc, char *argv[]) {


//    return 0;
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}