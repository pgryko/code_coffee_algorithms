#include <gtest/gtest.h>

#include <iostream>

#include "linkedlist.hpp"

using namespace std;

TEST(Node, TestSimpleNode) {
  struct Node<std::string> node = {
    "AA", nullptr
  };
  EXPECT_EQ("AA", node.data);
  EXPECT_EQ(nullptr, node.pNext);

  // Test that overloaded stream operators are configured correctly
  stringstream test;
  test << node;
  EXPECT_EQ("AA", test.str());

  struct Node<std::string> node2 = {
    "BB", nullptr
  };
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
  EXPECT_EQ(true, my_linked_list.Empty());
}

TEST(LinkedList, TestPush) {
  auto my_linked_list = LinkedList<std::string>();
  EXPECT_EQ(nullptr, my_linked_list.GetHeadNode());

  auto elements = std::array{"1", "2", "3", "4"};

  for (const auto &elem : elements) {
    my_linked_list.Push(elem);
  }
  EXPECT_EQ(4, my_linked_list.Size());

  std::reverse(elements.begin(), elements.end());
  auto pCrawler = my_linked_list.GetHeadNode();
  for (const auto &elem : elements) {
    EXPECT_EQ(elem, pCrawler->data);
    pCrawler = pCrawler->pNext;
  }
}

TEST(LinkedList, TestPop) {
  auto my_linked_list = LinkedList<std::string>();
  EXPECT_EQ(nullptr, my_linked_list.GetHeadNode());

  auto elements = std::array{"1", "2", "3", "4"};

  for (const auto &elem : elements) {
    my_linked_list.Push(elem);
  }
  EXPECT_EQ(4, my_linked_list.Size());

  std::reverse(elements.begin(), elements.end());
  for (const auto &elem : elements) {
    EXPECT_EQ(elem, my_linked_list.Pop());
  }
}

TEST(LinkedList, TestIterator) {
  auto my_linked_list = LinkedList<std::string>();
  EXPECT_EQ(nullptr, my_linked_list.GetHeadNode());

  auto elements = std::array{"1", "2", "3", "4"};

  for (const auto &elem : elements) {
    my_linked_list.Push(elem);
  }
  EXPECT_EQ(4, my_linked_list.Size());

  std::reverse(elements.begin(), elements.end());

  auto expected_iter = elements.begin();

  for (auto iter = my_linked_list.begin(); iter != my_linked_list.end();
       iter++, expected_iter++) {
    EXPECT_EQ(*iter, *expected_iter);
  };

  auto test_forward_overload = my_linked_list.begin();
  test_forward_overload++;
  EXPECT_EQ(*test_forward_overload, "3");
  ++test_forward_overload;
  EXPECT_EQ(*test_forward_overload, "2");
}

int main(int argc, char *argv[]) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}