import Sidebar from "@/components/Sidebar"
export default function DashboardLayout({children}: {children:React.ReactNode}){
    return (
        <div className="h-full flex flex-row ">
            <Sidebar />
            <div className="px-2 py-4">

            {children}
            </div>
        </div>
    )
}