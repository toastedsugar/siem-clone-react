import LogItemContainer from "@/components/LogItemContainer";

export default function Page(){
    return(
        <div className="flex flex-col gap-4">
            <LogItemContainer>
                Log 1
            </LogItemContainer>
            <LogItemContainer>
                Log 2
            </LogItemContainer>
            <LogItemContainer>
                Log 3
            </LogItemContainer>
            <LogItemContainer>
                Log 4
            </LogItemContainer>
        </div>
    )
}