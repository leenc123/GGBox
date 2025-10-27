import sys
import pkg_resources
def check_environment():
    required_packages = ['requests', 'beautifulsoup4']
    missing_packages = []
    
    for package in required_packages:
        try:
            pkg_resources.get_distribution(package)
            print(f"✅ {package} 已安装")
        except pkg_resources.DistributionNotFound:
            missing_packages.append(package)
            print(f"❌ {package} 未安装")
    
    if missing_packages:
        print(f"\n请安装缺失的包: pip install {' '.join(missing_packages)}")
        return False
    else:
        print("\n✅ 所有依赖包已安装，环境正常！")
        return True
if __name__ == '__main__':
    check_environment()