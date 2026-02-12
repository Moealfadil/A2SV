class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        output_img=[row[:] for row in img]
        for i in range(len(img)):
            for j in range(len(img[0])):
                current_sum=[]
                current_sum.append(img[i][j])
                if i-1 >= 0 and j-1 >= 0:
                    current_sum.append(img[i-1][j-1])
                if i-1 >= 0:
                    current_sum.append(img[i-1][j])
                if j-1 >= 0:
                    current_sum.append(img[i][j-1])
                if i+1 < len(img) and j+1 < len(img[0]):
                    current_sum.append(img[i+1][j+1])
                if i+1 < len(img) and j-1 >= 0:
                    current_sum.append(img[i+1][j-1])
                if i-1 >= 0 and j+1 < len(img[0]):
                    current_sum.append(img[i-1][j+1])
                if j+1 < len(img[0]):
                    current_sum.append(img[i][j+1])
                if i+1 < len(img):
                    current_sum.append(img[i+1][j])
                output_img[i][j]=sum(current_sum)//len(current_sum)
        return output_img