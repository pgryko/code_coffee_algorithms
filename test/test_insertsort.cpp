#include "gtest/gtest.h"
#include "insertsort.h"

TEST(insertsort, SortArray1) {
    std::array<int, 7> a1{5, 4, 2, 1, 6, 3, 1};
    std::array<int, 7> a2{5, 4, 2, 1, 6, 3, 1};
    std::array<int, 7> a3{5, 4, 2, 1, 6, 3, 1};
    insertsort(&a3);
    EXPECT_EQ(a1, a2);
}