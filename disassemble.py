#phase_1
   0x00005555555555e7 <+0>:	endbr64  # 分支目标缓冲区（BTB）技术，可以提高间接跳转和间接调用的性能
   0x00005555555555eb <+4>:	sub    $0x8,%rsp  # 将栈指针（%rsp）减去8，为接下来的调用函数预留空间
   0x00005555555555ef <+8>:	lea    0x1b56(%rip),%rsi        # 0x55555555714c   # 将相对指令指针（%rip）偏移0x1b56的地址加载到寄存器%rsi
   0x00005555555555f6 <+15>:	call   0x555555555bb5 <strings_not_equal> # 调用strings_not_equal函数，将输入字符串与期望字符串进行比较
   0x00005555555555fb <+20>:	test   %eax,%eax  # 检查上一个函数调用的返回值（%eax）是否为零
   0x00005555555555fd <+22>:	jne    0x555555555604 <phase_1+29>  # 如果上述test指令结果不为零（即字符串不相等），则跳转到地址0x555555555604
   0x00005555555555ff <+24>:	add    $0x8,%rsp  # 将栈指针（%rsp）增加8，回收之前为函数调用预留的空间
   0x0000555555555603 <+28>:	ret    
   0x0000555555555604 <+29>:	call   0x555555555cc9 <explode_bomb>   # 调用explode_bomb函数，表示炸弹被触发
   0x0000555555555609 <+34>:	jmp    0x5555555555ff <phase_1+24>  # 跳转到地址0x5555555555ff，返回到调用者
 #phase_2
   0x000055555555560b <+0>:	endbr64 
   0x000055555555560f <+4>:	push   %rbp # 将基指针（%rbp）压入栈中，保存现场
   0x0000555555555610 <+5>:	push   %rbx # 将寄存器（%rbx）压入栈中，保存现场
   0x0000555555555611 <+6>:	sub    $0x28,%rsp # 将栈指针（%rsp）减去40（0x28），为局部变量和调用函数预留空间
   0x0000555555555615 <+10>:	mov    %fs:0x28,%rax # 将fs段寄存器的偏移地址0x28处的值移动到%rax寄存器中，用于栈保护
   0x000055555555561e <+19>:	mov    %rax,0x18(%rsp)  # 将%rax的值存储到栈上的偏移位置0x18
   0x0000555555555623 <+24>:	xor    %eax,%eax  # 将%eax与自身异或，将寄存器%eax置零
   0x0000555555555625 <+26>:	mov    %rsp,%rsi  # 将栈指针（%rsp）的值复制到寄存器%rsi
   0x0000555555555628 <+29>:	call   0x555555555cf5 <read_six_numbers>  # 调用read_six_numbers函数，从输入中读取六个数字
   0x000055555555562d <+34>:	cmpl   $0x0,(%rsp)   # 比较栈顶的第一个数字是否为0
   0x0000555555555631 <+38>:	jne    0x55555555563a <phase_2+47>  # 如果第一个数字不为0，跳转到地址0x55555555563a
   0x0000555555555633 <+40>:	cmpl   $0x1,0x4(%rsp)   # 比较栈顶第二个数字是否为1
   0x0000555555555638 <+45>:	je     0x55555555563f <phase_2+52>  # 如果第二个数字等于1，跳转到地址0x55555555563f
   0x000055555555563a <+47>:	call   0x555555555cc9 <explode_bomb>
   0x000055555555563f <+52>:	mov    %rsp,%rbx  # 将栈指针（%rsp）的值复制到寄存器%rbx
   0x0000555555555642 <+55>:	lea    0x10(%rsp),%rbp  # 将栈指针（%rsp）偏移16（0x10）的地址加载到寄存器%rbp
   0x0000555555555647 <+60>:	jmp    0x555555555652 <phase_2+71>  # 直接跳转到地址0x555555555652
   0x0000555555555649 <+62>:	add    $0x4,%rbx  # 将寄存器%rbx的值加4
   0x000055555555564d <+66>:	cmp    %rbp,%rbx  # 比较寄存器%rbp和%rbx的值
   0x0000555555555650 <+69>:	je     0x555555555663 <phase_2+88>  # 如果%rbp等于%rbx，跳转到地址0x555555555663
   0x0000555555555652 <+71>:	mov    0x4(%rbx),%eax   # 将寄存器%rbx偏移4的值加载到%eax寄存器
   0x0000555555555655 <+74>:	add    (%rbx),%eax   # 将%rbx指向的值与%eax相加，结果存储在%eax中
   0x0000555555555657 <+76>:	cmp    %eax,0x8(%rbx)   # 比较%eax与%rbx偏移8处的值是否相等
   0x000055555555565a <+79>:	je     0x555555555649 <phase_2+62>  # 如果相等，跳转到地址0x555555555649
   0x000055555555565c <+81>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555661 <+86>:	jmp    0x555555555649 <phase_2+62>  # 跳转到地址0x555555555649
   0x0000555555555663 <+88>:	mov    0x18(%rsp),%rax  # 将栈上偏移位置0x18的值加载到%rax寄存器
   0x0000555555555668 <+93>:	sub    %fs:0x28,%rax # 将fs段寄存器的偏移地址0x28处的值从%rax中减去，用于栈保护检查
   0x0000555555555671 <+102>:	jne    0x55555555567a <phase_2+111> # 如果不相等，跳转到地址0x55555555567a
   0x0000555555555673 <+104>:	add    $0x28,%rsp # 将栈指针（%rsp）增加40（0x28），回收之前为局部变量和函数调用预留的空间
   0x0000555555555677 <+108>:	pop    %rbx # 将寄存器%rbx从栈中弹出，恢复现场
   0x0000555555555678 <+109>:	pop    %rbp # 将基指针（%rbp）从栈中弹出，恢复现场
   0x0000555555555679 <+110>:	ret    
   0x000055555555567a <+111>:	call   0x555555555250 <__stack_chk_fail@plt> # 调用栈保护失败函数，处理栈溢出攻击
#phase_3
   0x000055555555567f <+0>:	endbr64 
   0x0000555555555683 <+4>:	sub    $0x28,%rsp
   0x0000555555555687 <+8>:	mov    %fs:0x28,%rax
   0x0000555555555690 <+17>:	mov    %rax,0x18(%rsp)
   0x0000555555555695 <+22>:	xor    %eax,%eax
   0x0000555555555697 <+24>:	lea    0xf(%rsp),%rcx
   0x000055555555569c <+29>:	lea    0x10(%rsp),%rdx
   0x00005555555556a1 <+34>:	lea    0x14(%rsp),%r8
   0x00005555555556a6 <+39>:	lea    0x1abc(%rip),%rsi        # 0x555555557169
   0x00005555555556ad <+46>:	call   0x555555555300 <__isoc99_sscanf@plt>  # 将输入字符串解析为两个整数，存放在%rsp+0x10和%rsp+0x14
   0x00005555555556b2 <+51>:	cmp    $0x2,%eax  # 比较%eax（解析到的整数个数）是否大于2，如果小于等于2，则跳转到+88，触发炸弹
   0x00005555555556b5 <+54>:	jle    0x5555555556d7 <phase_3+88>
   0x00005555555556b7 <+56>:	cmpl   $0x7,0x10(%rsp)
   0x00005555555556bc <+61>:	ja     0x5555555557c8 <phase_3+329> # 比较x是否大于7，如果大于7，则跳转到+329，触发炸弹
   0x00005555555556c2 <+67>:	mov    0x10(%rsp),%eax
   0x00005555555556c6 <+71>:	lea    0x1ab3(%rip),%rdx        # 0x555555557180   #跳转表基址
   0x00005555555556cd <+78>:	movslq (%rdx,%rax,4),%rax
   0x00005555555556d1 <+82>:	add    %rdx,%rax
   0x00005555555556d4 <+85>:	notrack jmp *%rax
   0x00005555555556d7 <+88>:	call   0x555555555cc9 <explode_bomb>
   0x00005555555556dc <+93>:	jmp    0x5555555556b7 <phase_3+56>
   0x00005555555556de <+95>:	mov    $0x71,%eax # 将一个字节值存储到%eax寄存器中，这个值表示一个ASCII码
   0x00005555555556e3 <+100>:	cmpl   $0x1b4,0x14(%rsp)   # 0x14(%rsp)存储了第二个输入数字
   0x00005555555556eb <+108>:	je     0x5555555557d2 <phase_3+339>
   0x00005555555556f1 <+114>:	call   0x555555555cc9 <explode_bomb>
   0x00005555555556f6 <+119>:	mov    $0x71,%eax
   0x00005555555556fb <+124>:	jmp    0x5555555557d2 <phase_3+339>
   0x0000555555555700 <+129>:	mov    $0x6d,%eax
   0x0000555555555705 <+134>:	cmpl   $0x264,0x14(%rsp)
   0x000055555555570d <+142>:	je     0x5555555557d2 <phase_3+339>
   0x0000555555555713 <+148>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555718 <+153>:	mov    $0x6d,%eax
   0x000055555555571d <+158>:	jmp    0x5555555557d2 <phase_3+339>
   0x0000555555555722 <+163>:	mov    $0x67,%eax
   0x0000555555555727 <+168>:	cmpl   $0x2cf,0x14(%rsp)
   0x000055555555572f <+176>:	je     0x5555555557d2 <phase_3+339>
   0x0000555555555735 <+182>:	call   0x555555555cc9 <explode_bomb>
   0x000055555555573a <+187>:	mov    $0x67,%eax
   0x000055555555573f <+192>:	jmp    0x5555555557d2 <phase_3+339>
   0x0000555555555744 <+197>:	mov    $0x6f,%eax
   0x0000555555555749 <+202>:	cmpl   $0x347,0x14(%rsp)
   0x0000555555555751 <+210>:	je     0x5555555557d2 <phase_3+339>
   0x0000555555555753 <+212>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555758 <+217>:	mov    $0x6f,%eax
   0x000055555555575d <+222>:	jmp    0x5555555557d2 <phase_3+339>
   0x000055555555575f <+224>:	mov    $0x61,%eax
   0x0000555555555764 <+229>:	cmpl   $0x48,0x14(%rsp)
   0x0000555555555769 <+234>:	je     0x5555555557d2 <phase_3+339>
   0x000055555555576b <+236>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555770 <+241>:	mov    $0x61,%eax
   0x0000555555555775 <+246>:	jmp    0x5555555557d2 <phase_3+339>
   0x0000555555555777 <+248>:	mov    $0x61,%eax
   0x000055555555577c <+253>:	cmpl   $0x263,0x14(%rsp)
   0x0000555555555784 <+261>:	je     0x5555555557d2 <phase_3+339>
   0x0000555555555786 <+263>:	call   0x555555555cc9 <explode_bomb>
   0x000055555555578b <+268>:	mov    $0x61,%eax
   0x0000555555555790 <+273>:	jmp    0x5555555557d2 <phase_3+339>
   0x0000555555555792 <+275>:	mov    $0x65,%eax
   0x0000555555555797 <+280>:	cmpl   $0x2d6,0x14(%rsp)
   0x000055555555579f <+288>:	je     0x5555555557d2 <phase_3+339>
   0x00005555555557a1 <+290>:	call   0x555555555cc9 <explode_bomb>
   0x00005555555557a6 <+295>:	mov    $0x65,%eax
   0x00005555555557ab <+300>:	jmp    0x5555555557d2 <phase_3+339>
   0x00005555555557ad <+302>:	mov    $0x66,%eax
   0x00005555555557b2 <+307>:	cmpl   $0xed,0x14(%rsp)
   0x00005555555557ba <+315>:	je     0x5555555557d2 <phase_3+339>
   0x00005555555557bc <+317>:	call   0x555555555cc9 <explode_bomb>
   0x00005555555557c1 <+322>:	mov    $0x66,%eax
   0x00005555555557c6 <+327>:	jmp    0x5555555557d2 <phase_3+339>
   0x00005555555557c8 <+329>:	call   0x555555555cc9 <explode_bomb>
   0x00005555555557cd <+334>:	mov    $0x62,%eax
   0x00005555555557d2 <+339>:	cmp    %al,0xf(%rsp) # 指令+339至+343用于比较y与%x（一个存储在%rsp+0xf的字符）是否相等，如果不相等，则跳转到+366，触发炸弹
   0x00005555555557d6 <+343>:	jne    0x5555555557ed <phase_3+366>
   0x00005555555557d8 <+345>:	mov    0x18(%rsp),%rax
   0x00005555555557dd <+350>:	sub    %fs:0x28,%rax
   0x00005555555557e6 <+359>:	jne    0x5555555557f4 <phase_3+373>
   0x00005555555557e8 <+361>:	add    $0x28,%rsp
   0x00005555555557ec <+365>:	ret    
   0x00005555555557ed <+366>:	call   0x555555555cc9 <explode_bomb>
   0x00005555555557f2 <+371>:	jmp    0x5555555557d8 <phase_3+345>
   0x00005555555557f4 <+373>:	call   0x555555555250 <__stack_chk_fail@plt>
#phase_4
   0x000055555555583a <+0>:	endbr64 
   0x000055555555583e <+4>:	sub    $0x18,%rsp # 从输入中解析两个数字，分别存储在%rsp和0x4(%rsp)处
   0x0000555555555842 <+8>:	mov    %fs:0x28,%rax
   0x000055555555584b <+17>:	mov    %rax,0x8(%rsp)
   0x0000555555555850 <+22>:	xor    %eax,%eax
   0x0000555555555852 <+24>:	lea    0x4(%rsp),%rcx
   0x0000555555555857 <+29>:	mov    %rsp,%rdx
   0x000055555555585a <+32>:	lea    0x1a86(%rip),%rsi        # 0x5555555572e7
   0x0000555555555861 <+39>:	call   0x555555555300 <__isoc99_sscanf@plt>
   0x0000555555555866 <+44>:	cmp    $0x2,%eax
   0x0000555555555869 <+47>:	jne    0x555555555871 <phase_4+55>
   0x000055555555586b <+49>:	cmpl   $0xe,(%rsp)   # 检查第一个数字是否小于等于14（0xe）
   0x000055555555586f <+53>:	jbe    0x555555555876 <phase_4+60>
   0x0000555555555871 <+55>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555876 <+60>:	mov    $0xe,%edx
   0x000055555555587b <+65>:	mov    $0x0,%esi
   0x0000555555555880 <+70>:	mov    (%rsp),%edi
   0x0000555555555883 <+73>:	call   0x5555555557f9 <func4> # 调用func4，传递三个参数：%edi（第一个数字）、%esi（0）和%edx（14）
   0x0000555555555888 <+78>:	cmp    $0x6,%eax  # 检查func4的返回值（%eax）是否等于6
   0x000055555555588b <+81>:	jne    0x555555555894 <phase_4+90>
   0x000055555555588d <+83>:	cmpl   $0x6,0x4(%rsp)
   0x0000555555555892 <+88>:	je     0x555555555899 <phase_4+95>
   0x0000555555555894 <+90>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555899 <+95>:	mov    0x8(%rsp),%rax
   0x000055555555589e <+100>:	sub    %fs:0x28,%rax
   0x00005555555558a7 <+109>:	jne    0x5555555558ae <phase_4+116>
   0x00005555555558a9 <+111>:	add    $0x18,%rsp
   0x00005555555558ad <+115>:	ret    
   0x00005555555558ae <+116>:	call   0x555555555250 <__stack_chk_fail@plt>
#func4
   0x00005555555557f9 <+0>:	endbr64 
   0x00005555555557fd <+4>:	sub    $0x8,%rsp  
   0x0000555555555801 <+8>:	mov    %edx,%eax
   0x0000555555555803 <+10>:	sub    %esi,%eax
   0x0000555555555805 <+12>:	mov    %eax,%ecx
   0x0000555555555807 <+14>:	shr    $0x1f,%ecx
   0x000055555555580a <+17>:	add    %eax,%ecx
   0x000055555555580c <+19>:	sar    %ecx
   0x000055555555580e <+21>:	add    %esi,%ecx
   0x0000555555555810 <+23>:	cmp    %edi,%ecx
   0x0000555555555812 <+25>:	jg     0x555555555820 <func4+39>
   0x0000555555555814 <+27>:	mov    $0x0,%eax
   0x0000555555555819 <+32>:	jl     0x55555555582c <func4+51>
   0x000055555555581b <+34>:	add    $0x8,%rsp
   0x000055555555581f <+38>:	ret    
   0x0000555555555820 <+39>:	lea    -0x1(%rcx),%edx
   0x0000555555555823 <+42>:	call   0x5555555557f9 <func4>
   0x0000555555555828 <+47>:	add    %eax,%eax
   0x000055555555582a <+49>:	jmp    0x55555555581b <func4+34>
   0x000055555555582c <+51>:	lea    0x1(%rcx),%esi
   0x000055555555582f <+54>:	call   0x5555555557f9 <func4>
   0x0000555555555834 <+59>:	lea    0x1(%rax,%rax,1),%eax
   0x0000555555555838 <+63>:	jmp    0x55555555581b <func4+34>
#phase_5
   0x00005555555558b3 <+0>:	endbr64 
   0x00005555555558b7 <+4>:	push   %rbx
   0x00005555555558b8 <+5>:	sub    $0x10,%rsp
   0x00005555555558bc <+9>:	mov    %rdi,%rbx
   0x00005555555558bf <+12>:	mov    %fs:0x28,%rax
   0x00005555555558c8 <+21>:	mov    %rax,0x8(%rsp)
   0x00005555555558cd <+26>:	xor    %eax,%eax
   0x00005555555558cf <+28>:	call   0x555555555b94 <string_length>
   0x00005555555558d4 <+33>:	cmp    $0x6,%eax
   0x00005555555558d7 <+36>:	jne    0x55555555592e <phase_5+123>
   0x00005555555558d9 <+38>:	mov    $0x0,%eax
   0x00005555555558de <+43>:	lea    0x18bb(%rip),%rcx        # 0x5555555571a0 <array.0>
   0x00005555555558e5 <+50>:	movzbl (%rbx,%rax,1),%edx
   0x00005555555558e9 <+54>:	and    $0xf,%edx
   0x00005555555558ec <+57>:	movzbl (%rcx,%rdx,1),%edx
   0x00005555555558f0 <+61>:	mov    %dl,0x1(%rsp,%rax,1)
   0x00005555555558f4 <+65>:	add    $0x1,%rax
   0x00005555555558f8 <+69>:	cmp    $0x6,%rax
   0x00005555555558fc <+73>:	jne    0x5555555558e5 <phase_5+50>
   0x00005555555558fe <+75>:	movb   $0x0,0x7(%rsp)
   0x0000555555555903 <+80>:	lea    0x1(%rsp),%rdi
   0x0000555555555908 <+85>:	lea    0x1863(%rip),%rsi        # 0x555555557172
   0x000055555555590f <+92>:	call   0x555555555bb5 <strings_not_equal>
   0x0000555555555914 <+97>:	test   %eax,%eax
   0x0000555555555916 <+99>:	jne    0x555555555935 <phase_5+130>
   0x0000555555555918 <+101>:	mov    0x8(%rsp),%rax
   0x000055555555591d <+106>:	sub    %fs:0x28,%rax
   0x0000555555555926 <+115>:	jne    0x55555555593c <phase_5+137>
   0x0000555555555928 <+117>:	add    $0x10,%rsp
   0x000055555555592c <+121>:	pop    %rbx
   0x000055555555592d <+122>:	ret    
   0x000055555555592e <+123>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555933 <+128>:	jmp    0x5555555558d9 <phase_5+38>
   0x0000555555555935 <+130>:	call   0x555555555cc9 <explode_bomb>
   0x000055555555593a <+135>:	jmp    0x555555555918 <phase_5+101>
   0x000055555555593c <+137>:	call   0x555555555250 <__stack_chk_fail@plt>
#phase_6
   0x0000555555555941 <+0>:	endbr64 
   0x0000555555555945 <+4>:	push   %r14
   0x0000555555555947 <+6>:	push   %r13
   0x0000555555555949 <+8>:	push   %r12
   0x000055555555594b <+10>:	push   %rbp
   0x000055555555594c <+11>:	push   %rbx
   0x000055555555594d <+12>:	sub    $0x60,%rsp
   0x0000555555555951 <+16>:	mov    %fs:0x28,%rax
   0x000055555555595a <+25>:	mov    %rax,0x58(%rsp)
   0x000055555555595f <+30>:	xor    %eax,%eax
   0x0000555555555961 <+32>:	mov    %rsp,%r13
   0x0000555555555964 <+35>:	mov    %r13,%rsi
   0x0000555555555967 <+38>:	call   0x555555555cf5 <read_six_numbers>
   0x000055555555596c <+43>:	mov    $0x1,%r14d
   0x0000555555555972 <+49>:	mov    %rsp,%r12
   0x0000555555555975 <+52>:	jmp    0x55555555599f <phase_6+94>
   0x0000555555555977 <+54>:	call   0x555555555cc9 <explode_bomb>
   0x000055555555597c <+59>:	jmp    0x5555555559ae <phase_6+109>
   0x000055555555597e <+61>:	add    $0x1,%rbx
   0x0000555555555982 <+65>:	cmp    $0x5,%ebx
   0x0000555555555985 <+68>:	jg     0x555555555997 <phase_6+86>
   0x0000555555555987 <+70>:	mov    (%r12,%rbx,4),%eax
   0x000055555555598b <+74>:	cmp    %eax,0x0(%rbp)
   0x000055555555598e <+77>:	jne    0x55555555597e <phase_6+61>
   0x0000555555555990 <+79>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555995 <+84>:	jmp    0x55555555597e <phase_6+61>
   0x0000555555555997 <+86>:	add    $0x1,%r14
   0x000055555555599b <+90>:	add    $0x4,%r13
   0x000055555555599f <+94>:	mov    %r13,%rbp
   0x00005555555559a2 <+97>:	mov    0x0(%r13),%eax
   0x00005555555559a6 <+101>:	sub    $0x1,%eax
   0x00005555555559a9 <+104>:	cmp    $0x5,%eax
   0x00005555555559ac <+107>:	ja     0x555555555977 <phase_6+54>
   0x00005555555559ae <+109>:	cmp    $0x5,%r14d
   0x00005555555559b2 <+113>:	jg     0x5555555559b9 <phase_6+120>
   0x00005555555559b4 <+115>:	mov    %r14,%rbx
   0x00005555555559b7 <+118>:	jmp    0x555555555987 <phase_6+70>
   0x00005555555559b9 <+120>:	mov    $0x0,%esi
   0x00005555555559be <+125>:	mov    (%rsp,%rsi,4),%ecx
   0x00005555555559c1 <+128>:	mov    $0x1,%eax
   0x00005555555559c6 <+133>:	lea    0x3843(%rip),%rdx        # 0x555555559210 <node1>
   0x00005555555559cd <+140>:	cmp    $0x1,%ecx
   0x00005555555559d0 <+143>:	jle    0x5555555559dd <phase_6+156>
   0x00005555555559d2 <+145>:	mov    0x8(%rdx),%rdx
   0x00005555555559d6 <+149>:	add    $0x1,%eax
   0x00005555555559d9 <+152>:	cmp    %ecx,%eax
   0x00005555555559db <+154>:	jne    0x5555555559d2 <phase_6+145>
   0x00005555555559dd <+156>:	mov    %rdx,0x20(%rsp,%rsi,8)
   0x00005555555559e2 <+161>:	add    $0x1,%rsi
   0x00005555555559e6 <+165>:	cmp    $0x6,%rsi
   0x00005555555559ea <+169>:	jne    0x5555555559be <phase_6+125>
   0x00005555555559ec <+171>:	mov    0x20(%rsp),%rbx
   0x00005555555559f1 <+176>:	mov    0x28(%rsp),%rax
   0x00005555555559f6 <+181>:	mov    %rax,0x8(%rbx)
   0x00005555555559fa <+185>:	mov    0x30(%rsp),%rdx
   0x00005555555559ff <+190>:	mov    %rdx,0x8(%rax)
   0x0000555555555a03 <+194>:	mov    0x38(%rsp),%rax
   0x0000555555555a08 <+199>:	mov    %rax,0x8(%rdx)
   0x0000555555555a0c <+203>:	mov    0x40(%rsp),%rdx
   0x0000555555555a11 <+208>:	mov    %rdx,0x8(%rax)
   0x0000555555555a15 <+212>:	mov    0x48(%rsp),%rax
   0x0000555555555a1a <+217>:	mov    %rax,0x8(%rdx)
   0x0000555555555a1e <+221>:	movq   $0x0,0x8(%rax)
   0x0000555555555a26 <+229>:	mov    $0x5,%ebp
   0x0000555555555a2b <+234>:	jmp    0x555555555a36 <phase_6+245>
   0x0000555555555a2d <+236>:	mov    0x8(%rbx),%rbx
   0x0000555555555a31 <+240>:	sub    $0x1,%ebp
   0x0000555555555a34 <+243>:	je     0x555555555a47 <phase_6+262>
   0x0000555555555a36 <+245>:	mov    0x8(%rbx),%rax
   0x0000555555555a3a <+249>:	mov    (%rax),%eax
   0x0000555555555a3c <+251>:	cmp    %eax,(%rbx)
   0x0000555555555a3e <+253>:	jle    0x555555555a2d <phase_6+236>
   0x0000555555555a40 <+255>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555a45 <+260>:	jmp    0x555555555a2d <phase_6+236>
   0x0000555555555a47 <+262>:	mov    0x58(%rsp),%rax
   0x0000555555555a4c <+267>:	sub    %fs:0x28,%rax
   0x0000555555555a55 <+276>:	jne    0x555555555a64 <phase_6+291>
   0x0000555555555a57 <+278>:	add    $0x60,%rsp
   0x0000555555555a5b <+282>:	pop    %rbx
   0x0000555555555a5c <+283>:	pop    %rbp
   0x0000555555555a5d <+284>:	pop    %r12
   0x0000555555555a5f <+286>:	pop    %r13
   0x0000555555555a61 <+288>:	pop    %r14
   0x0000555555555a63 <+290>:	ret    
   0x0000555555555a64 <+291>:	call   0x555555555250 <__stack_chk_fail@plt>
#phase_defused
   0x0000555555555e72 <+0>:	endbr64 
   0x0000555555555e76 <+4>:	sub    $0x78,%rsp
   0x0000555555555e7a <+8>:	mov    %fs:0x28,%rax
   0x0000555555555e83 <+17>:	mov    %rax,0x68(%rsp)
   0x0000555555555e88 <+22>:	xor    %eax,%eax
   0x0000555555555e8a <+24>:	cmpl   $0x6,0x385f(%rip)        # 0x5555555596f0 <num_input_strings>
   0x0000555555555e91 <+31>:	je     0x555555555ea8 <phase_defused+54>
   0x0000555555555e93 <+33>:	mov    0x68(%rsp),%rax
   0x0000555555555e98 <+38>:	sub    %fs:0x28,%rax
   0x0000555555555ea1 <+47>:	jne    0x555555555f16 <phase_defused+164>
   0x0000555555555ea3 <+49>:	add    $0x78,%rsp
   0x0000555555555ea7 <+53>:	ret    
   0x0000555555555ea8 <+54>:	lea    0xc(%rsp),%rcx
   0x0000555555555ead <+59>:	lea    0x8(%rsp),%rdx
   0x0000555555555eb2 <+64>:	lea    0x10(%rsp),%r8
   0x0000555555555eb7 <+69>:	lea    0x1473(%rip),%rsi        # 0x555555557331
   0x0000555555555ebe <+76>:	lea    0x392b(%rip),%rdi        # 0x5555555597f0 <input_strings+240>
   0x0000555555555ec5 <+83>:	call   0x555555555300 <__isoc99_sscanf@plt>
   0x0000555555555eca <+88>:	cmp    $0x3,%eax
   0x0000555555555ecd <+91>:	je     0x555555555edd <phase_defused+107>
   0x0000555555555ecf <+93>:	lea    0x139a(%rip),%rdi        # 0x555555557270
   0x0000555555555ed6 <+100>:	call   0x555555555220 <puts@plt>
   0x0000555555555edb <+105>:	jmp    0x555555555e93 <phase_defused+33>
   0x0000555555555edd <+107>:	lea    0x10(%rsp),%rdi
   0x0000555555555ee2 <+112>:	lea    0x1451(%rip),%rsi        # 0x55555555733a
   0x0000555555555ee9 <+119>:	call   0x555555555bb5 <strings_not_equal>
   0x0000555555555eee <+124>:	test   %eax,%eax
   0x0000555555555ef0 <+126>:	jne    0x555555555ecf <phase_defused+93>
   0x0000555555555ef2 <+128>:	lea    0x1317(%rip),%rdi        # 0x555555557210
   0x0000555555555ef9 <+135>:	call   0x555555555220 <puts@plt>
   0x0000555555555efe <+140>:	lea    0x1333(%rip),%rdi        # 0x555555557238
   0x0000555555555f05 <+147>:	call   0x555555555220 <puts@plt>
   0x0000555555555f0a <+152>:	mov    $0x0,%eax
   0x0000555555555f0f <+157>:	call   0x555555555aaa <secret_phase>
   0x0000555555555f14 <+162>:	jmp    0x555555555ecf <phase_defused+93>
   0x0000555555555f16 <+164>:	call   0x555555555250 <__stack_chk_fail@plt>
#secret_phase
   0x0000555555555aaa <+0>:	endbr64 
   0x0000555555555aae <+4>:	push   %rbx
   0x0000555555555aaf <+5>:	call   0x555555555d3a <read_line>
   0x0000555555555ab4 <+10>:	mov    %rax,%rdi
   0x0000555555555ab7 <+13>:	mov    $0xa,%edx
   0x0000555555555abc <+18>:	mov    $0x0,%esi
   0x0000555555555ac1 <+23>:	call   0x5555555552e0 <strtol@plt>
   0x0000555555555ac6 <+28>:	mov    %eax,%ebx
   0x0000555555555ac8 <+30>:	sub    $0x1,%eax
   0x0000555555555acb <+33>:	cmp    $0x3e8,%eax
   0x0000555555555ad0 <+38>:	ja     0x555555555af7 <secret_phase+77>
   0x0000555555555ad2 <+40>:	mov    %ebx,%esi
   0x0000555555555ad4 <+42>:	lea    0x3655(%rip),%rdi        # 0x555555559130 <n1>
   0x0000555555555adb <+49>:	call   0x555555555a69 <fun7>
   0x0000555555555ae0 <+54>:	test   %eax,%eax
   0x0000555555555ae2 <+56>:	jne    0x555555555afe <secret_phase+84>
   0x0000555555555ae4 <+58>:	lea    0x16c5(%rip),%rdi        # 0x5555555571b0
   0x0000555555555aeb <+65>:	call   0x555555555220 <puts@plt>
   0x0000555555555af0 <+70>:	call   0x555555555e72 <phase_defused>
   0x0000555555555af5 <+75>:	pop    %rbx
   0x0000555555555af6 <+76>:	ret    
   0x0000555555555af7 <+77>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555afc <+82>:	jmp    0x555555555ad2 <secret_phase+40>
   0x0000555555555afe <+84>:	call   0x555555555cc9 <explode_bomb>
   0x0000555555555b03 <+89>:	jmp    0x555555555ae4 <secret_phase+58>
#fun7
   0x0000555555555a69 <+0>:	endbr64 
   0x0000555555555a6d <+4>:	test   %rdi,%rdi
   0x0000555555555a70 <+7>:	je     0x555555555aa4 <fun7+59>
   0x0000555555555a72 <+9>:	sub    $0x8,%rsp
   0x0000555555555a76 <+13>:	mov    (%rdi),%edx
   0x0000555555555a78 <+15>:	cmp    %esi,%edx
   0x0000555555555a7a <+17>:	jg     0x555555555a88 <fun7+31>
   0x0000555555555a7c <+19>:	mov    $0x0,%eax
   0x0000555555555a81 <+24>:	jne    0x555555555a95 <fun7+44>
   0x0000555555555a83 <+26>:	add    $0x8,%rsp
   0x0000555555555a87 <+30>:	ret    
   0x0000555555555a88 <+31>:	mov    0x8(%rdi),%rdi
   0x0000555555555a8c <+35>:	call   0x555555555a69 <fun7>
   0x0000555555555a91 <+40>:	add    %eax,%eax
   0x0000555555555a93 <+42>:	jmp    0x555555555a83 <fun7+26>
   0x0000555555555a95 <+44>:	mov    0x10(%rdi),%rdi
   0x0000555555555a99 <+48>:	call   0x555555555a69 <fun7>
   0x0000555555555a9e <+53>:	lea    0x1(%rax,%rax,1),%eax
   0x0000555555555aa2 <+57>:	jmp    0x555555555a83 <fun7+26>
   0x0000555555555aa4 <+59>:	mov    $0xffffffff,%eax
   0x0000555555555aa9 <+64>:	ret    
