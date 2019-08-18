/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxLevelSum(root *TreeNode) int {
	// bfs
	queue := []*TreeNode{root}
	sum := root.Val
	level := 1
	ans := 1
	for len(queue) > 0 {
		levelSum := 0
		nextLevel := []*TreeNode{}
		for i := 0; i < len(queue); i++ {
			cur := queue[i]
			levelSum += cur.Val
			if cur.Left != nil {
				nextLevel = append(nextLevel, cur.Left)
			}
			if cur.Right != nil {
				nextLevel = append(nextLevel, cur.Right)
			}
		}
		if levelSum > sum {
			ans = level
			sum = levelSum
		}
		level += 1
		queue = nextLevel
	}
	return ans
}
