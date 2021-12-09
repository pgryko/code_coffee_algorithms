#include <gtest/gtest.h>

#include <iostream>

#include "hashchaining.hpp"

TEST(HashChaining, TestInitialisation) {
  auto hashmap_empty = HashChaining<std::string, std::string>();
  EXPECT_EQ(hashmap_empty.Count(), 0);
  auto hashmap = HashChaining<std::string, std::string>("AAA", "Value123");
  EXPECT_EQ(hashmap.Count(), 1);
}

TEST(HashChaining, TestGet) {
  auto hashmap_empty = HashChaining<std::string, std::string>();

  auto value_empty = hashmap_empty.Get("AAA");

  EXPECT_EQ(value_empty.first, "");
  EXPECT_EQ(value_empty.second, "");

  auto hashmap = HashChaining<std::string, std::string>("AAA", "ValueAAA");

  auto value = hashmap.Get("AAA");

  EXPECT_EQ(value.first, "AAA");
  EXPECT_EQ(value.second, "ValueAAA");

  auto elements =
      std::array{"AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III"};

  for (const auto &elem : elements) {
    hashmap.Push(elem, std::string("Value").append(elem));
  }
  EXPECT_EQ(9, hashmap.Count());
}

TEST(HashChaining, TestExists) {
  auto hashmap_empty = HashChaining<std::string, std::string>();
  EXPECT_FALSE(hashmap_empty.Exists("AAA"));
  EXPECT_FALSE(hashmap_empty.Exists(""));

  auto hashmap = HashChaining<std::string, std::string>("AAA", "Value123");

  EXPECT_TRUE(hashmap.Exists("AAA"));
  EXPECT_FALSE(hashmap.Exists("AAAB"));
}

TEST(HashChaining, TestPush) {
  // Test Building from empty constructor
  auto hashmap_empty = HashChaining<std::string, std::string>();
  EXPECT_FALSE(hashmap_empty.Exists("AAA"));
  EXPECT_FALSE(hashmap_empty.Exists(""));
  EXPECT_EQ(hashmap_empty.Count(), 0);

  hashmap_empty.Push("AAA", "ValueAAA");
  EXPECT_TRUE(hashmap_empty.Exists("AAA"));
  EXPECT_FALSE(hashmap_empty.Exists("AAAB"));
  EXPECT_EQ(hashmap_empty.Count(), 1);

  // Test double push, should not re-add
  hashmap_empty.Push("AAA", "ValueAAA");
  EXPECT_TRUE(hashmap_empty.Exists("AAA"));
  EXPECT_EQ(hashmap_empty.Count(), 1);

  // Test pushing next element
  hashmap_empty.Push("BBB", "ValueBBB");
  EXPECT_TRUE(hashmap_empty.Exists("BBB"));
  EXPECT_EQ(hashmap_empty.Count(), 2);

  // Default container size is 7, so by pushing 9 elements,
  // we guarantee either a resize or collisions occurring
  // Note the attempted double push of BBB again
  auto elements =
      std::array{"BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III"};

  for (const auto &elem : elements) {
    hashmap_empty.Push(elem, std::string("Value").append(elem));
  }
  EXPECT_EQ(9, hashmap_empty.Count());

  // Test building with constructor initialization
  auto hashmap = HashChaining<std::string, std::string>("AAA", "Value123");

  EXPECT_TRUE(hashmap.Exists("AAA"));
  EXPECT_FALSE(hashmap.Exists("AAAB"));

  elements = std::array{"BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III"};

  for (const auto &elem : elements) {
    hashmap.Push(elem, std::string("Value").append(elem));
  }
  EXPECT_EQ(9, hashmap.Count());

  for (const auto &elem : elements) {
    EXPECT_TRUE(hashmap.Exists(elem));
  }
};

TEST(HashChaining, TestChaining) {
  // Test an inherited class where the resize function is overwritten to do
  // nothing. This essentially forces chaining to occur as we are pushing more
  // elements than in container capacity
  auto hashmap_no_resize = TESTHashChaining<std::string, std::string>();
  EXPECT_EQ(hashmap_no_resize.Capacity(), 7);

  auto elements =
      std::array{"AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III"};

  for (const auto &elem : elements) {
    hashmap_no_resize.Push(elem, std::string("Value").append(elem));
  }
  EXPECT_EQ(9, hashmap_no_resize.Count());

  for (const auto &elem : elements) {
    EXPECT_TRUE(hashmap_no_resize.Exists(elem));
  }

  EXPECT_EQ(hashmap_no_resize.Capacity(), 7);
}

TEST(HashChaining, TestResize) {
  // Same test as above but test that resize has occurred correctly
  auto hashmap = HashChaining<std::string, std::string>();
  EXPECT_EQ(hashmap.Capacity(), 7);

  auto elements =
      std::array{"AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III"};

  for (const auto &elem : elements) {
    hashmap.Push(elem, std::string("Value").append(elem));
  }
  EXPECT_EQ(9, hashmap.Count());

  for (const auto &elem : elements) {
    EXPECT_TRUE(hashmap.Exists(elem));
  }

  // Expect two resizes
  EXPECT_EQ(hashmap.Capacity(), 31);
}

TEST(HashChaining, TestRemove) {
  // Test building with constructor initialization
  auto hashmap = HashChaining<std::string, std::string>();

  auto elements =
      std::array{"AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III"};

  for (const auto &elem : elements) {
    hashmap.Push(elem, std::string("Value").append(elem));
  }
  EXPECT_EQ(9, hashmap.Count());

  for (const auto &elem : elements) {
    EXPECT_TRUE(hashmap.Exists(elem));
  }

  // Test that attempting to remove a non existing key, returns false
  EXPECT_FALSE(hashmap.Remove("AFK"));
  EXPECT_EQ(9, hashmap.Count());

  // Remove keys
  for (const auto &elem : elements) {
    EXPECT_TRUE(hashmap.Remove(elem));
  }

  EXPECT_EQ(0, hashmap.Count());

  // Re-add them
  for (const auto &elem : elements) {
    hashmap.Push(elem, std::string("Value").append(elem));
  }
  EXPECT_EQ(9, hashmap.Count());

  for (const auto &elem : elements) {
    EXPECT_TRUE(hashmap.Exists(elem));
  }
}

int main(int argc, char *argv[]) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
};